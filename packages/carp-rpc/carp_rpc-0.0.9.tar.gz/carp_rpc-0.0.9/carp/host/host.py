import threading
import queue
import asyncio
from collections import defaultdict
import inspect
import random

from uuid import uuid4

from carp.service import (
    ApiFunction,
    ApiMethod,
    ApiNonInstanceMethod,
    CallData,
    CallResponse,
)
from carp.channel import Channel, ChannelError
from carp.serializer import Serializer, Serializable


class RemoteExecutionError(Exception):
    pass


class HostAnnounce(Serializable):
    def __init__(self, *, host_id):
        self.host_id = host_id
        super().__init__()

    def to_dict(self):
        return dict(
            host_id=self.host_id
        )


class HostExports(Serializable):
    def __init__(self, *, host_id, exports, metadata):
        self.host_id = host_id
        self.exports = exports
        self.metadata = metadata
        super().__init__()

    def to_dict(self):
        return dict(
            host_id=self.host_id,
            exports=self.exports,
            metadata=self.metadata,
        )


class HostExitNotify(Serializable):
    def __init__(self, *, host_id):
        self.host_id = host_id

    def to_dict(self):
        return dict(host_id=self.host_id)


class Host:
    STOPPED = "stopped"
    STARTED = "started"

    def __init__(
        self, *,
        label=None,
    ):
        self.id = uuid4().hex
        self.label = label or self.id

        self.services_remote = defaultdict(list)
        self.services_local = {}
        self.services_event = asyncio.Event()
        self.hosts_errored = set()
        self.calls_active = {}
        self.hosts_remote = {}
        self.listen_channel = None
        self.task_last_id = 0
        self.tasks = {}
        self.status = Host.STOPPED

        self.event_loop_thread = threading.get_ident()
        self.event_loop = asyncio.get_event_loop()

        # callbacks
        self.event_handlers = defaultdict(list)

    async def _report_services(self):
        host_map = HostExports(
            host_id=self.id,
            exports=list(self.services_local.keys()),
            metadata={
                service_name: service.metadata
                for service_name, service in self.services_local.items()
            }
        ).serialize()
        for channel in self.hosts_remote.values():
            await channel.put(host_map)

    async def _set_status(self, new_status, **kwargs):
        old_status = self.status
        self.status = new_status
        await self.emit("status", old_status, new_status, **kwargs)

    async def _task_wrapper(self, coro, task_id):
        rv = None
        try:
            rv = await coro
        except Exception as e:
            import traceback
            tbinfo = traceback.format_exc()
            await self.emit("exception", e, tbinfo)
        finally:
            if task_id in self.tasks:
                del self.tasks[task_id]
        return rv

    def async_task(self, coro):
        if inspect.isawaitable(coro):
            current_thread = threading.get_ident()
            task_id = self.task_last_id
            self.task_last_id += 1

            if current_thread == self.event_loop_thread:
                task = asyncio.create_task(self._task_wrapper(coro, task_id))
            else:
                task = asyncio.run_coroutine_threadsafe(
                    self._task_wrapper(coro, task_id), self.event_loop
                )
            self.tasks[task_id] = task
            return task
        else:
            return coro

    async def start(self, channel: Channel):
        """
        Start the host, accepting connections on the specified
        Channel
        """
        self.listen_channel = channel
        await channel.serve(on_connect=self.accept)
        await self._set_status(Host.STARTED)

    async def stop(self):
        to_cancel = self.tasks.values()
        self.tasks = {}
        for t in to_cancel:
            if t.done() and t.exception() is not None:
                await self.emit("exception", t.exception(), None)
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass
            except:
                await self.emit("exception", t.exception(), None)
        await self._set_status(Host.STOPPED)

    async def accept(self, channel):
        await self.emit("accept", channel)
        await channel.put(HostAnnounce(host_id=self.id).serialize())
        await self._message_loop(channel)

    async def connect(self, channel):
        await self._set_status(Host.STARTED)
        await channel.connect()
        await self.emit("connect", channel)

        await channel.put(HostAnnounce(host_id=self.id).serialize())
        self.async_task(self._message_loop(channel))

    async def _message_loop(self, channel):
        async def _process(bdata):
            message = Serializer.deserialize(bdata)

            try:
                await self.emit("message", message)
            except ValueError as e:
                await self.emit("exception", e, None)
                return

            try:
                if isinstance(message, HostAnnounce):
                    self.hosts_remote[message.host_id] = channel
                    await self._report_services()
                elif isinstance(message, HostExitNotify):
                    for service, hosts in self.services_remote.items():
                        if message.host_id in hosts:
                            hosts.remove(message.host_id)
                elif isinstance(message, HostExports):
                    for service in message.exports:
                        if message.host_id not in self.services_remote[service]:
                            self.services_remote[service].append(message.host_id)
                    await self.emit(
                        "exports", message.host_id,
                        message.exports, message.metadata
                    )
                    self.services_event.set()
                elif isinstance(message, CallData):
                    await self.emit("call", message)
                    service = self.services_local.get(
                        message.service_name.split(".")[0]
                    )
                    if not service:
                        raise RemoteExecutionError(
                            f"Service {message.service_name} not on {self.id}"
                        )
                    response = await self.handle(service, message)
                    await channel.put(response.serialize())

                elif isinstance(message, CallResponse):
                    call_data = self.calls_active.get(message.call_id)
                    # FIXME: Should not be returning CallResponses for
                    # no response methods
                    if call_data:
                        call_data.response = message
                        call_data.event.set()
            except Exception as e:
                to_close = []
                for host_id in list(self.hosts_remote.keys()):
                    remote_channel = self.hosts_remote[host_id]
                    if remote_channel == channel:
                        to_close.append((host_id, remote_channel))

                for host_id, remote_channel in to_close:
                    del self.hosts_remote[host_id]
                    for service_name in list(self.services_remote.keys()):
                        providers = self.services_remote[service_name]
                        if providers and host_id in providers:
                            new_prov = [
                                p for p in providers if p != host_id
                            ]
                            if new_prov:
                                self.services_remote[service_name] = new_prov
                            else:
                                del self.services_remote[service_name]

                    await self.emit("disconnect", host_id)

        first_message = True
        while (
            self.status == Host.STARTED
            and channel.status == Channel.CONNECTED
        ):
            try:
                message_bytes = await channel.get()
                if first_message:
                    await _process(message_bytes)
                    first_message = False
                else:
                    self.async_task(_process(message_bytes))
            except Exception as e:
                to_close = []
                for host_id in list(self.hosts_remote.keys()):
                    remote_channel = self.hosts_remote[host_id]
                    if remote_channel == channel:
                        to_close.append((host_id, remote_channel))
                        remote_channel.status = Channel.CLOSED
                for host_id, remote_channel in to_close:
                    del self.hosts_remote[host_id]
                    for service_name in list(self.services_remote.keys()):
                        providers = self.services_remote[service_name]
                        if providers and host_id in providers:
                            new_prov = [
                                p for p in providers if p != host_id
                            ]
                            if new_prov:
                                self.services_remote[service_name] = new_prov
                            else:
                                del self.services_remote[service_name]
                    await self.emit("disconnect", host_id)

        await channel.close()

    async def export(self, service_impl, metadata=None):
        """
        Announce that a service is available on this host
        """
        api_factory = ApiFunction
        if hasattr(service_impl, '_service_type'):
            api_factory = service_impl._service_type

        service = api_factory(service_impl)
        if metadata:
            service.metadata = metadata

        self.services_local[service.name] = service
        service.is_remote = False
        service.host = self
        service.host_id = self.id
        await self._report_services()
        self.services_event.set()
        return service

    async def require(self, service_impl, host_id=None):
        """
        Use a service announced by this or another host, waiting
        until it is available
        """
        api_factory = ApiFunction
        if hasattr(service_impl, '_service_type'):
            api_factory = service_impl._service_type

        service = api_factory(service_impl)

        while (
            service.name not in self.services_local
            and service.name not in self.services_remote
            and self.status == Host.STARTED
        ):
            await self.services_event.wait()
            self.services_event.clear()

        service.host = self
        if service.name in self.services_local:
            service.is_remote = False
            service.host_id = self.id
        elif service.name in self.services_remote:
            if not host_id:
                host_id = random.choice(self.services_remote[service.name])
            service.host_id = host_id
            service.is_remote = True

        return service

    async def call(
        self, service, args, kwargs, *,
        response=True, response_queue=None, response_callback=None
    ):
        """
        Send a request to a remote service, waiting for a
        response
        """

        call_data = CallData(
            service_name=service.name,
            host_id=service.host_id,
            instance_id=service.instance_id,
            args=args,
            kwargs=kwargs
        )
        channel = self.hosts_remote.get(service.host_id)
        if not channel:
            if service.host_id not in self.hosts_errored:
                await self.emit("error", f"Service {service.name} host {service.host_id} disappeared")
                self.hosts_errored.add(service.host_id)
            return None

        if response:
            self.calls_active[call_data.call_id] = call_data

        try:
            await channel.put(call_data.serialize())
        except Exception as e:
            import traceback
            tbinfo = traceback.format_exc()
            await self.emit("exception", e, tbinfo)
            exception = type(e).__name__

        if response:
            await call_data.event.wait()
            del self.calls_active[call_data.call_id]

            if call_data.response.exception:
                raise RemoteExecutionError(call_data.response.exception)
            if response_queue:
                response_queue.put(call_data.response.value)
            if response_callback:
                response_callback(call_data.response.value)

            return call_data.response.value

        if response_queue:
            response_queue.put(None)
        return None

    def call_with_cb(self, service, args, kwargs, *, callback=None):
        """
        Non-blocking synchronous call with callback for response
        """
        self.async_task(
            self.call(
                service, args, kwargs, response=True,
                response_callback=callback,
            )
        )
        return None

    def call_blocking(self, service, args, kwargs, response=True):
        """
        Synchronous version of call() for bridging to non-async-aware
        processes
        """
        response_queue = None
        rv = None

        if response:
            response_queue = queue.Queue(1)

        self.async_task(
            self.call(
                service, args, kwargs, response=response,
                response_queue=response_queue,
            )
        )

        if response:
            rv = response_queue.get()
        return rv

    async def handle(self, service, message):
        """
        Handle a remote request using a local service
        """
        call_return = None
        exception = None

        if service.name != message.service_name:
            method_name = message.service_name.split(".", 1)[1]
            class_service = service

            # FIXME should have a better way of getting the right
            # service from the CallData
            if message.instance_id:
                service = ApiMethod(
                    class_service, method_name, message.instance_id
                )
            else:
                service = ApiNonInstanceMethod(class_service, method_name)

        try:
            raw_return = service(*message.args, **message.kwargs)
            if inspect.isawaitable(raw_return):
                call_return = await raw_return
            else:
                call_return = raw_return

        except Exception as e:
            import traceback
            tbinfo = traceback.format_exc()
            await self.emit("exception", e, tbinfo)
            exception = type(e).__name__

        return CallResponse(
            call_id=message.call_id,
            service_name=service.name,
            host_id=message.host_id,
            value=call_return,
            exception=exception,
        )

    def on(self, event_name, handler, uninstall=False):
        prev = self.event_handlers[event_name]
        if not uninstall:
            prev.append(handler)
        else:
            self.event_handlers[event_name] = filter(
                lambda h: h != handler, prev
            )

    async def emit(self, event_name, *args, **kwargs):
        handlers = self.event_handlers[event_name]
        for handler in handlers:
            handled = handler(event_name, *args, **kwargs)
            if inspect.isawaitable(handled):
                handled = await handled
            if handled:
                break

    async def wait_for_completion(self):
        while tasks := self.tasks.values():
            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
            for task in done:
                if task.exception() is not None:
                    self.emit("exception", task.exception(), None)
