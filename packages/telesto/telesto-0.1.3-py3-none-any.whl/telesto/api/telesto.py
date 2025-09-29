# Telesto
# Copyright (C) 2025  Visual Topology Ltd
#
# MIT License
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

import os
import logging
import sys

from typing import Literal,Any

from narvi.api.narvi_server import NarviServer
from hyrrokkin.execution_manager.process_runner import ProcessRunner
from narvi.utils.resource_loader import ResourceLoader
from telesto.workspace.telesto_workspace import TelestoWorkspace, DIRECTORY_APP_NAME


class Telesto:

    def __init__(self, configurations:dict[str,dict[str,Any]], workspace_root_folder:str=None, host:str="localhost", port:int=8889, base_url:str="",
                 include_packages:list[str]=[], exclude_packages:list[str]=[], launch_ui:str=None,
                 monitoring:tuple[int,int]=(0,0), main_workspace_id:str=None, in_process:bool=False, use_server:Literal["auto","tornado", "builtin"]="auto"):
        """
        Create and operate a telesto service comprised of one or more workspaces and (optionally) a monitoring service

        Args:
            configurations: a dictionary mapping from workspace id to the workspace configuration (usually loaded from the workspace TOML file)
            workspace_root_folder: (optional) Use this folder as a parent folder for all workspaces which have a relative workspace path
            host: the hostname at which the service will listen
            port: the port number at which the service will listen
            base_url: specify the base URL at which workspaces will be "mounted"
            include_packages: list of additional packages to include in this workspace
            exclude_packages: list of patterns to match packages to exclude
            launch_ui: specify a command launch a web browser on startup, for example \"chromium --app=URL\".  URL will be substituted for the url of the first workspace's directory.
            monitoring: enable narvi service monitoring with the specified interval and retention period (in seconds) set either to zero to disable monitoring
            main_workspace_id: If multiple workspaces are defined, use this to specify a main one
            in_process: Run engines in process (if possible)
            use_server: Use the specified web-server (auto, tornado, builtin).  Auto will select tornado if installed.
        """
        self.logger = logging.getLogger("telesto")
        self.host = host
        self.port = port
        self.base_url = base_url
        self.monitoring = monitoring
        self.launch_ui = launch_ui
        if self.base_url.endswith("/"):
            self.base_url = self.base_url[:-1]

        self.workspace_root_folder = workspace_root_folder

        self.workspaces = {}
        workspace_paths = {}

        self.main_workspace_id = main_workspace_id

        for configuration in configurations:
            workspace_id = configuration["workspace_id"]

            if workspace_id in self.workspaces:
                self.logger.error(f"Multiple workspaces configured with id {workspace_id}")
                sys.exit(1)

            if self.main_workspace_id is None:
                self.main_workspace_id = workspace_id

            workspace = TelestoWorkspace(workspace_id=workspace_id,
                             configuration=configuration, workspace_root_folder=workspace_root_folder,
                             base_url=self.base_url, include_packages=include_packages,
                             exclude_packages=exclude_packages, in_process=in_process)

            self.workspaces[workspace_id] = workspace

            abs_workspace_path = os.path.abspath(workspace.get_path())
            if abs_workspace_path in workspace_paths:
                self.logger.error(f"Multiple workspaces ({workspace_id},{workspace_paths[abs_workspace_path]}) are configured with the same path ({abs_workspace_path})")
                sys.exit(1)
            else:
                workspace_paths[abs_workspace_path] = workspace_id

        self.server = None

        if use_server == "builtin":
            self.web_server_type = "builtin"
        else:
            try:
                # if tornado is installed, use it
                import tornado
                self.web_server_type = "tornado"
            except:
                if use_server == "auto":
                    # if not, fallback to narvi's builtin webserver
                    self.logger.info("tornado web-server not installed, falling back to builtin web-server")
                    self.web_server_type = "builtin"
                else:
                    self.logger.error("tornado web-server requested but tornado is not installed")
                    raise

    def run(self):

        self.logger.info(f"Starting telesto at {self.host}:{self.port}/{self.base_url}")

        monitoring_options = {}
        monitoring_enabled = False
        if self.monitoring[0] > 0 and self.monitoring[1] > 0:
            monitoring_enabled = True
            monitoring_options["admin_path"] = "/status.json"
            monitoring_options["monitoring_interval_s"] = self.monitoring[0]
            monitoring_options["monitoring_retention_s"] = self.monitoring[1]

        self.server = NarviServer(host=self.host, port=self.port, web_server_type=self.web_server_type,
                             base_path=self.base_url, **monitoring_options)

        for workspace in self.workspaces.values():
            workspace.bind(self.server)

        # setup shortcuts to the main workspace (if defined) directory
        if self.main_workspace_id:
            self.server.register_redirect(self.base_url + "/index.html", self.main_workspace_id,
                                      DIRECTORY_APP_NAME)
            self.server.register_redirect(self.base_url + "/", self.main_workspace_id, DIRECTORY_APP_NAME)

        # add a monitor service and app
        if monitoring_enabled:
            app_service = self.server.register_service(workspace="system_workspace",
                                                       app_cls_name="narvi.apps.monitor.monitor_app.MonitorApp",
                                                       app_service_name="monitor_service",
                                                       fixed_service_id="monitor", shared_service=True)

            self.server.register_app(application_service=app_service, app_name="monitor_app",
                                     app_parameters={},
                                     resource_roots={
                                         "index.html": ResourceLoader.get_path_of_resource("narvi.apps.monitor",
                                                                                           "index.html"),
                                         "monitor_app.js": ResourceLoader.get_path_of_resource("narvi.apps.monitor",
                                                                                               "monitor_app.js"),
                                         ("narvi", "*"): ResourceLoader.get_path_of_resource("narvi.static")
                                     })

        def list_services():
            app_details = sorted(self.server.list_app_urls(), key=lambda t: t[0])
            for (workspace, app_name, url) in app_details:
                if workspace and workspace != "system_workspace":
                    self.logger.info(f"{workspace}:{app_name} => {url}")

            for (workspace, app_name, url) in app_details:
                if workspace == "system_workspace":
                    self.logger.info(f"{workspace}:{app_name} => {url}")

            for (workspace, app_name, url) in app_details:
                if workspace == "":
                    self.logger.info(f"{app_name} => {url}")

        # called when the web server is listening
        def open_callback():
            list_services()
            if self.launch_ui and self.main_workspace_id:
                # open a web browser on the directory of the first workspace
                local_url = f"http://{self.host}:{self.port}{self.base_url}/{self.main_workspace_id}/{DIRECTORY_APP_NAME}/index.html"
                cmd = self.launch_ui.replace("URL",local_url)
                pr = ProcessRunner(cmd.split(" "), exit_callback=lambda: self.server.close())
                pr.start()

        self.server.run(open_callback)


