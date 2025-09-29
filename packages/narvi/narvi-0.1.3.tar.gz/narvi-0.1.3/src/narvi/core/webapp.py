# MIT License
#
# Narvi - a simple python web application server
#
# Copyright (C) 2022-2025 Visual Topology Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import threading
import time
import logging
import datetime
import queue

from narvi.commands.webapp_message import WebappMessage

from narvi.commands.connect_session import ConnectSession
from narvi.commands.disconnect_session import DisconnectSession
from narvi.commands.handler_request import HandlerRequest
from narvi.commands.handler_response import HandlerResponse
from narvi.commands.session_connected import SessionConnected
from narvi.commands.app2app_message import App2AppMessage

from narvi.services.webapp_services import WebAppServices
from narvi.utils.resource_loader import ResourceLoader


class WebApp(threading.Thread):

    def __init__(self, workspace, app_name, app_id, app_cls_name, app_parameters={},
                 register_request_handler_callback=None, unregister_request_handler_callback=None,
                 service_id=None, app2app_sender=None):

        super().__init__()
        self.workspace = workspace
        self.app_name = app_name
        self.app_id = app_id
        self.app_cls_name = app_cls_name
        self.application_service = app_cls_name
        self.app_parameters = app_parameters
        self.service_id = service_id
        self.app2app_sender = app2app_sender

        self.metrics_callback = None
        self.metrics_metadata = None

        self.sessions = {}  # session_id => send function with args (msg)
        self.eventq = queue.Queue()  # tuple(from-session-id,cmd,aux) for inbound (from session)
        # and (None,cmd,aux) for outbound (to session)

        self.close_on_session_end = False

        self.daemon = True
        self.start_time = datetime.datetime.now()
        self.logger = logging.getLogger("App:"+self.app_name)
        self.register_request_handler_callback = register_request_handler_callback
        self.unregister_request_handler_callback = unregister_request_handler_callback
        self.session_open_listeners = set()
        self.session_close_listeners = set()
        self.app_close_listeners = set()
        self.message_listeners = set()
        self.app2app_message_callback = None
        self.webapp_services = WebAppServices(self, workspace, service_id)
        cls = ResourceLoader.get_class(self.app_cls_name)
        self.request_handlers = {}  # handler_id => callback
        self.session_request_handlers = {}
        self.admin_listener = None
        self.idle_timeout = None
        self.idle_start = None
        self.instance = cls(self.webapp_services, **app_parameters)

    def get_instance(self):
        return self.instance

    def get_start_time(self):
        return self.start_time

    def dispatch_handle_request(self, method, handler_id, path_parameters, query_parameters, headers, request_body):
        response_q = queue.Queue()
        self.enqueue("0", HandlerRequest(method, handler_id, path_parameters, query_parameters, headers, request_body, response_q))
        response = response_q.get()
        return (response.http_code, response.content_bytes, response.mime_type, response.response_headers)

    def send_to_app(self, to_workspace_id, to_app_name, to_service_id, data):
        if self.app2app_sender:
            return self.app2app_sender(to_workspace_id, to_app_name, to_service_id, data)
        return False

    def set_app2app_message_callback(self, app2app_message_callback):
        self.app2app_message_callback = app2app_message_callback

    def receive_from_app(self, from_workspace_id, from_app_name, from_service_id, data):
        self.enqueue(None, App2AppMessage(from_workspace_id, from_app_name, from_service_id, data))

    def set_close_on_session_end(self):
        self.close_on_session_end = True

    def set_idle_timeout(self, idle_timeout):
        self.idle_timeout = idle_timeout

    def check_idle(self):
        if self.idle_timeout is not None and len(self.sessions) == 0:
            if (self.idle_start is not None and time.time() - self.idle_start > self.idle_timeout):
                self.logger.debug("Closing app due to idle timeout")
                self.stop()

    def get_name(self):
        return self.app_name

    def get_id(self):
        return self.app_id

    def get_key(self):
        return (self.workspace, self.app_name, self.service_id)

    def set_metrics_callback(self, metrics_callback, metrics_metadata):
        self.metrics_callback = metrics_callback
        self.metrics_metadata = metrics_metadata

    def get_metrics(self):
        if self.metrics_callback:
            try:
                return self.metrics_callback()
            except Exception as ex:
                import traceback
                traceback.print_exception(ex)
        return None

    def get_metrics_metadata(self):
        return self.metrics_metadata

    def set_admin_listener(self, callback):
        self.admin_listener = callback

    def get_admin_listener(self):
        return self.admin_listener

    def receive_session_message(self, session_id, msg):
        # receive a message from a session
        if msg == "":
            pass  # heartbeat, ignore
        else:
            cmd = WebappMessage(msg, from_session_id=session_id)
            self.enqueue(session_id, cmd)

    def connect(self, app_name, app_parameters, session_id, query_parameters, headers, send_fn):
        self.enqueue(session_id, ConnectSession(app_name, app_parameters, session_id, query_parameters, headers, send_fn))

    def disconnect(self, session_id):
        self.enqueue(session_id, DisconnectSession(session_id))

    def send_webapp_message(self, msg, for_session_id=None, except_session_id=None):
        self.enqueue(None, WebappMessage(msg, for_session_id=for_session_id, except_session_id=except_session_id))

    def enqueue(self, session_id, cmd, aux=None):
        self.eventq.put((session_id, cmd, aux))

    def create_request_service(self, app_name, handler_pattern, method, handler, session_id=None):
        url = ""
        if session_id:
            url += f"session/{session_id}/"
        url += handler_pattern
        handler_id = self.register_request_handler_callback(app_name, handler_pattern, method, self.service_id, session_id)
        self.request_handlers[(handler_id)] = handler
        if session_id:
            self.session_request_handlers[(handler_id,session_id)] = handler
        return handler_id, url

    def remove_request_service(self, handler_id):
        if handler_id in self.request_handlers:
            del self.request_handlers[handler_id]
        for (session_handler_id, session_id) in self.session_request_handlers:
            if session_handler_id == handler_id:
                del self.session_request_handlers[(session_handler_id,session_id)]
        self.unregister_request_handler_callback(handler_id)

    def run(self):
        while True:
            try:
                (session_id, cmd, aux) = self.eventq.get(timeout=10)
            except queue.Empty:
                self.check_idle()
                continue

            self.check_idle()
            if session_id is None and cmd is None:
                break
            if session_id:
                # message is coming into the app from a client session
                self.logger.debug("<= " + str(cmd))
                self.handle_session_command(session_id,cmd,aux)
            else:
                # message is emitted by the app towards client session(s) or passing between apps
                self.logger.debug("=> " + str(cmd))
                self.handle_app_command(cmd,aux)

        for callback in self.app_close_listeners:
            try:
                callback()
            except Exception as ex:
                self.logger.exception("app_close_callback")
        self.logger.debug("Closed app")

    def handle_session_command(self,session_id,cmd,aux):
        if isinstance(cmd, ConnectSession):
            self.handle_connect_session(cmd.app_name, cmd.app_parameters, cmd.get_session_id(), cmd.get_query_parameters(), cmd.get_headers(), cmd.get_send_fn())
        elif isinstance(cmd, DisconnectSession):
            self.handle_disconnect_session(cmd.get_session_id())
        elif isinstance(cmd, WebappMessage):
            self.handle_webapp_message_command(cmd,session_id)
        elif isinstance(cmd, HandlerRequest):
            self.handle_request(cmd.method, cmd.handler_id, cmd.path_parameters, cmd.query_parameters, cmd.headers, cmd.request_body, cmd.response_q)
        else:
            self.logger.error(f"handle_session_command: unrecognized command {cmd}")

    def handle_request(self, method, handler_id, path_parameters, query_parameters, headers, request_body, response_q):
        if handler_id in self.request_handlers:
            (code, content_bytes, mime_type, response_headers) = self.request_handlers[handler_id](path_parameters,query_parameters,headers,request_body)
            response_q.put(HandlerResponse(code, content_bytes, mime_type, response_headers))
        else:
            response_q.put(HandlerResponse(404, b'NOT FOUND', "text/plain", {}))

    def handle_disconnect_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
        if self.close_on_session_end:
            self.stop()
        elif self.idle_timeout is not None:
            if len(self.sessions) == 0:
                self.idle_start = time.time()

    def handle_webapp_message_command(self,cmd,session_id):
        for message_listener in self.message_listeners:
            message_listener(cmd.get_message(), session_id)

    def handle_app_command(self,cmd, aux):
        if isinstance(cmd,SessionConnected):
            if cmd.session_id in self.sessions:
                self.sessions[cmd.session_id](cmd)
        elif isinstance(cmd,DisconnectSession):
            if cmd.session_id in self.sessions:
                self.sessions[cmd.session_id](cmd)
                del self.sessions[cmd.session_id]
        elif isinstance(cmd,WebappMessage):
            for_sid = cmd.get_for_session_id()
            exc_sid = cmd.get_except_session_id()
            for (session_id, send_fn) in self.sessions.items():
                if for_sid:
                    if session_id == for_sid:
                        send_fn(cmd)
                elif exc_sid:
                    if session_id != exc_sid:
                        send_fn(cmd)
                else:
                    send_fn(cmd)
        elif isinstance(cmd, App2AppMessage):
            if self.app2app_message_callback:
                self.app2app_message_callback(cmd.get_from_workspace_id(), cmd.get_from_app_name(), cmd.get_from_service_id(), cmd.get_data())
        else:
            self.logger.error(f"handle_app_command failed, unrecognized command {cmd}")

    def handle_connect_session(self, app_name, app_parameters, session_id, query_parameters, headers, send_fn):
        self.sessions[session_id] = send_fn
        self.open_session(app_name, session_id, query_parameters, headers)
        send_fn(SessionConnected(session_id, app_parameters))

    def add_session_open_listener(self, callback):
        self.session_open_listeners.add(callback)

    def add_session_close_listener(self, callback):
        self.session_close_listeners.add(callback)

    def add_message_listener(self, callback):
        self.message_listeners.add(callback)

    def add_app_close_listener(self, callback):
        self.app_close_listeners.add(callback)

    def open_session(self, app_name, session_id, query_parameters, headers):
        for callback in self.session_open_listeners:
            callback(app_name, session_id, query_parameters, headers)

    def close_session(self, session_id):
        for callback in self.session_close_listeners:
            callback(session_id)
        # remove any request services associated with this session
        for (handler_id, sid) in self.session_request_handlers:
            if sid == session_id:
                self.remove_request_service(handler_id)

    def close(self):
        try:
            for session_id in self.sessions:
                self.enqueue(None, DisconnectSession(session_id))
        finally:
            pass

        # remove all request handlers
        for (handler_id) in list(self.request_handlers):
            self.remove_request_service(handler_id)

        self.stop()

    def stop(self):
        self.enqueue(None, None)








