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

from typing import Any, Callable, Union
import logging

from narvi.core.registered_service import RegisteredService
from narvi.core.service import Service
from narvi.utils.resource_loader import ResourceLoader

JsonType = Union[dict[str, "JsonType"], list["JsonType"], str, int, float, bool, None]

class NarviServer:

    def __init__(self, host: str = "localhost", port: int = 8999, web_server_type: str = "tornado",
                 base_path: str = "/narvi", admin_path:str=None, monitoring_interval_s:int=None,
                 monitoring_retention_s:int=None):
        """
        Constructs a Narvi app server

        Args:
            host: hostname to run server, for example "localhost" or "0.0.0.0"
            port: port number for the servier, for example, 8080
            web_server_type: either "tornado" (recommended) or "builtin"
            base_path: the base url for all narvi URLs, should start with a leading "/"
            admin_path: path to listen at for admin requests
            monitoring_interval_s: the interval in seconds to poll webapps for metrics, or None to turn off monitoring
            monitoring_retention_s: discard metrics collected more than this many seconds ago, or None to never discard
        """
        self.service = Service(host=host, port=port, base_path=base_path,
                               web_server_type=web_server_type,
                               admin_path=admin_path,
                               monitoring_interval=monitoring_interval_s,
                               monitoring_retention=monitoring_retention_s)
        self.logger = logging.getLogger("NaviServer")

    def register_service(self, workspace:str, app_service_name:str, app_cls_name:str, app_parameters:dict[str,Any]={},
                         fixed_service_id:str=None, shared_service:bool=True, service_id_validator:Callable[[str],bool]=lambda service_id:True,
                         idle_timeout:int=3600) -> RegisteredService:
        """
        Register an application service backend.  Websocket connections can be made to this service at URL

        base_path + /$workspace/$app_service_name/$service_id/connect

        Args:
            workspace: a string identifying a workspace within which the app will be registered.  The workspace may be used as a security context.
            app_service_name: the name of the app
            app_cls_name: the resource path and name of the class implementing the web app name, eg foo.bar.foobar.FooBar
            app_parameters: a set of parameters passed to the app constructor
            fixed_service_id:  set this parameter if the service instances will be associated with this service id only
            shared_service: whether the service allows multiple connections to the same service instance
            service_id_validator: a callable which validates the service id
            idle_timeout: for shared services with no fixed service id - close the service after this delay once the last client disconnects

        Returns:
            a RegisteredService instance
        """
        return self.service.register_service(workspace=workspace, app_service_name=app_service_name, app_cls_name=app_cls_name,
                                             app_parameters=app_parameters, fixed_service_id=fixed_service_id,
                                             shared_service=shared_service, service_id_validator=service_id_validator,
                                             idle_timeout=idle_timeout)

    def register_app(self, app_name:str, application_service:RegisteredService, app_parameters:dict[str,JsonType]={},
                     resource_roots:dict[str|tuple[str,str],str]={}, service_chooser_app_name:str=None):
        """
        Register a web application frontend.  The application can be loaded from the following URL

        base_path + /$workspace/$app_service_name/$service_id/index.html
            or
        base_path + /$workspace/$app_service_name/index.html

        Args:
            app_name: the name of the app
            application_service: the name of the backend application service this frontend will connect to
            app_parameters: parameters to pass to the web application when constructed
            resource_roots: a dictionary mapping from a URL (relative to the application URL) to a filesystem path
                            eg individual files: { "images/icon.png": "/full/path/to/images/icon.png" }
                            or folders: { ("images","*.png"): "/full/path/to/images" }
                            both of these definitions will load URL images/icon.png from /full/path/to/images/icon.png
                            but the second definition will load all png images files from that folder
            service_chooser_app_name: the name of an app to redirect to if the service id is not provided by a connecting client
        """

        self.service.register_app(app_name, application_service=application_service,
                                  app_parameters=app_parameters,
                                  resource_roots=resource_roots,
                                  service_chooser_app_name=service_chooser_app_name)

    def register_redirect(self, from_url:str, to_workspace:str, to_app:str):
        """
        Create a redirection from the given URL to a given workspace and app

        Args:
            from_url: the URL to redirect, for example foo/bar
            to_workspace: the target workspace
            to_app: the target application name
        """
        self.service.register_redirect(from_url, to_workspace, to_app)

    def list_app_urls(self) -> list[tuple[str,str,str]]:
        """
        Find out which services are available

        Returns:
            a list of tuples (workspace, app_name, url) describing the apps that are registered
        """
        return self.service.get_summary()

    def run(self, ready_callback:Callable[[],None]=None):
        """
        Run the server

        Args:
            ready_callback: optional, a function that will be called when the server is listening and ready to accept connections
        """
        self.service.run(ready_callback)

    def start_service(self, workspace:str, app_service_name:str, service_id:str):
        """
        Start an instance of a service running

        Args:
            workspace: the workspace within which the service will run
            app_service_name: the name of the application service - must match a registered application service
            service_id: the service id for the service
        """
        self.service.start_service(workspace, app_service_name, service_id)

    def restart_service(self, workspace:str, app_service_name:str, service_id:str):
        """
        Restart a service

        Args:
            workspace: the workspace within which the service is running
            app_service_name: the name of the application service
            service_id: the service id
        """
        self.service.restart_service(workspace, app_service_name, service_id)

    def stop_service(self, workspace:str, app_service_name:str, service_id:str):
        """
        Stop a service

        Args:
            workspace: the workspace within which the service is running
            app_service_name: the name of the application service
            service_id: the service id
        """
        self.service.stop_service(workspace, app_service_name, service_id)

    def get_service_statuses(self, for_workspace:str) -> dict[str,JsonType]:
        """
        Get details of all services running in the workspace

        Args:
            for_workspace: the workspace to get details for

        Returns:
            dictionary mapping from service_id to service details for running services only
        """
        return self.service.get_admin_data(for_workspace=for_workspace)

    def close(self):
        """
        Stop and close this server.
        """
        self.service.close()

    def get_path_of_resource(self, package:str, resource:str="") -> str:
        """
        Gets the filesystem path to a python package or a resource within the package

        Args:
            package: the package name, expressed using dotted notation, for example module1.submoduleA
            resource: optional, provides the name of a file within the resource to load

        Returns:
            the filesystem path to the package directory or resource file.

        Raises:
            ModuleNotFoundError: if no package could be found
        """
        return ResourceLoader.get_path_of_resource(package, resource)


