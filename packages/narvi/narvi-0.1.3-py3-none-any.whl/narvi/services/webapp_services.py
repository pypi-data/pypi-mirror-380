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

from typing import Union, Callable, Any

"""
Defines a set of services that can be called by a web application.  When a web application is instantiated by narvi,
a services object is passed into the constructor.
"""

class WebAppServices:

    def __init__(self, webapp:"narvi.core.webapp.WebApp", workspace:str, service_id:str):
        self.app = webapp
        self.workspace = workspace
        self.service_id = service_id

    def create_request_service(self, app_name:str, handler_pattern:str,
                               handler: Callable[[dict[str, str],dict[str, str],dict[str, str], bytes], tuple[int, bytes, str, dict[str, str]]],
                               request_method:str="GET", session_id:str=None) -> tuple[str,str]:
        """
        Create a request service and return a URL to it

        Args:
            app_name: the name of the application associated with this service
            handler_pattern: specify a sub-path for the service, for example a/$b/c where components starting with $ will be resolved to request parameters
            handler: A function called when a user requests the service.  The callback is passed path parameters, request parameters, a dictionary containing HTTP headers from the request and the request body
                and should return a 4-tuple with components (response_code, binary_content, mime_type, response-headers)
            request_method: the method eg "GET", "PUT"
            session_id: the session id, if known
        Returns:
            a (handler-id, URL) that points to the created service endpoint.  The URL is relative to the app URL.
        """
        return self.app.create_request_service(app_name, handler_pattern, request_method, handler, session_id)

    def remove_request_service(self, handler_id:str):
        """
        Remove a request handler that was created by calling create_request_service

        Args:
            handler_id: the handler id returned from create_request_service when the service was created.
        """
        self.app.remove_request_service(handler_id)

    def send(self, msg:Union[str,bytes], for_session_id:str=None, except_session_id:str=None):
        """
        Send a message to the client peer (javascript) instance running in one or more client sessions

        Args:
            msg: str or bytes to send
            for_session_id: if specified, send to only this session
            except_session_id: if specified, send to all sessions except this one

        Notes:
            If both for_session_id and except_session_id are provided, except_session_id is ignored
        """
        self.app.send_webapp_message(msg, for_session_id=for_session_id, except_session_id=except_session_id)

    def add_message_listener(self, callback:Callable[[Union[str,bytes],str],None]):
        """
        Register a callback which is invoked when a message from a client peer (javascript) instance is received

        Args:
            callback: a function to call when a message is received, passing in the message content and originating session id
        """
        self.app.add_message_listener(callback)

    def add_session_open_listener(self, callback:Callable[[str,str,dict[str,str],dict[str,str]],None]):
        """
        Register a callback which is invoked when a session is opened

        Args:
            callback: a function to call when the event occurs, passing in the application name, session id, query parameters and the request headers
        """
        self.app.add_session_open_listener(callback)

    def add_session_close_listener(self, callback:Callable[[str],None]):
        """
        Register a callback which is invoked when a session is closed

        Args:
            callback: a function to call when the event occurs, passing in the session id
        """
        self.app.add_session_close_listener(callback)

    def set_metrics_callback(self, callback:Callable[[],dict[str,Any]], metrics_metadata:dict[str,dict[str,Any]]):
        """
        Register a callback which is invoked to obtain performance metrics for this instance.  This callback will be periodically
        called from a monitoring thread.

        Args:
            callback: a function to call, accepting no arguments, and returning a JSON-serialisable object mapping from metric name to value
            metrics_metadata: a dict mapping from metric name to a dict with keys "min", "max", "colour" which describe that metric
        """
        self.app.set_metrics_callback(callback, metrics_metadata)

    def set_app2app_message_callback(self, callback:Callable[[str,str,str,Any],None]):
        """
        Register a callback which is invoked when a message from another app is received

        Args:
            callback: function to be invoked when a message from another app is forwarded
                      parameters are, sending workspace_id, sending app_name, sending service_id, message data
        """
        self.app.set_app2app_message_callback(callback)

    def set_admin_listener(self, callback:Callable[[dict[str,Any]],None]):
        """
        Register a callback which is invoked with the latest admin information on all apps/services, including metrics

        Args:
            callback: a function to call, accepting no arguments, and returning a JSON-serialisable object
        """
        self.app.set_admin_listener(callback)

    def add_app_close_listener(self, callback:Callable[[],None]):
        """
        Register a callback which is invoked when the application instance is about to be closed

        Args:
            callback: a function to call when the event occurs, accepting no arguments
        """
        self.app.add_app_close_listener(callback)

    def get_service_id(self) -> str:
        """
        Gets the service id associated with this instance of the app service

        Returns:
            string containing the service id
        """
        return self.service_id

    def get_workspace_id(self) -> str:
        """
        Gets the workspace id in which this instance of the app service is running

        Returns:
            string containing the workspace id
        """
        return self.workspace

    def get_app_name(self) -> str:
        """
        Gets the application service name of this application service

        Returns:
            string containing the app name
        """
        return self.app.get_name()

    def send_to_app(self, workspace_id:str, app_name:str, service_id:str, data:Any) -> bool:
        """
        Send a message to another app

        Args:
            workspace_id: the workspace id of the app
            app_name: the application name
            service_id: the service id
            data: the data to send in the message

        Returns:
            True iff the receiving service instance was located to receive the message, False otherwise
        """
        return self.app.send_to_app(to_workspace_id=workspace_id, to_app_name=app_name, to_service_id=service_id, data=data)



