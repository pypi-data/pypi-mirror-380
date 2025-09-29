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
import json
import logging
import sys
import importlib.metadata
import fnmatch

from telesto.app_services.topology_directory import TopologyDirectory
from telesto.utils.telesto_utils import TelestoUtils
from hyrrokkin.utils.type_hints import JsonType

DESIGNER_APP_NAME = "topology_designer"
DIRECTORY_APP_NAME = "topology_directory"

RUNNER_SERVICE_NAME = "topology_runner"
DIRECTORY_SERVICE_NAME = "topology_directory"

class TelestoWorkspace:

    def __init__(self, workspace_id:str, configuration:dict[str,JsonType], workspace_root_folder:str=None, base_url:str="",
                 include_packages:list[str]=[], exclude_packages:list[str]=[], in_process:bool=False):
        """
        Create and operate a telesto workspace

        Args:
            workspace_id: the unique identifier for the workspace
            configuration: a dictionary configuring the workspace, loaded from the workspace's TOML file
            workspace_root_folder: (optional) Use this folder as a parent folder for all workspaces which have a relative workspace path
            base_url: specify the base URL at which the workspace is "mounted"
            include_packages: list of additional packages to include in this workspace
            exclude_packages: list of patterns to match packages to exclude
            in_process: Run engines in process (if possible)
        """

        self.base_url = base_url
        self.logger = logging.getLogger(f"telesto[{workspace_id}]")
        self.logger.info(f"Creating workspace {workspace_id}")
        self.workspace_id = workspace_id
        self.workspace_name = configuration.get("workspace_name","")
        self.workspace_description = configuration.get("workspace_description", "")
        self.idle_timeout = configuration.get("idle_timeout", 60)
        self.autostart = configuration.get("autostart",[])

        # work out where this workspace's files will be stored
        self.workspace_path = configuration.get("workspace_path", ".")
        if not os.path.isabs(self.workspace_path) and workspace_root_folder is not None:
            self.workspace_path = os.path.join(workspace_root_folder, self.workspace_path)

        self.applications = configuration.get("application", {})

        self.package_lists = {}

        self.server = None

        self.skadi_options = {}
        self.skadi_options["workspace_id"] = workspace_id
        self.skadi_options["designer_title"] = configuration.get("designer_title", "Telesto Designer")
        self.skadi_options["directory_title"] = configuration.get("directory_title", "Telesto Directory")
        self.skadi_options["designer_splash"] = configuration.get("directory_splash", {})
        self.skadi_options["directory_splash"] = configuration.get("directory_splash", {})
        self.package_list = configuration.get("include_packages", [])

        for include_package in include_packages:
            if include_package not in self.package_list:
                self.package_list.append(include_package)

        # add in all packages installed with the telesto_packages entrypoint...
        eps = importlib.metadata.entry_points()
        package_entrypoints = eps.select(group="telesto_packages")
        for entrypoint in package_entrypoints:
            if entrypoint.value not in self.package_list:
                self.package_list.append(entrypoint.value)

        # now remove any packages that were explicitly excluded...
        exclude_package_list = configuration.get("exclude_packages", []) + exclude_packages
        for excluded_package_pattern in exclude_package_list:
            packages = self.package_list[:]
            for package in packages:
                if fnmatch.fnmatch(package, excluded_package_pattern):
                    self.package_list.remove(package)

        if len(self.package_list) == 0:
            self.logger.warning(f"\tNo packages loaded for workspace {workspace_id}")

        self.hyrrokkin_options = {}
        self.hyrrokkin_options["in_process"] = in_process

        self.templates = configuration.get("template", {})

        self.package_folders = {}
        self.packages = {}

        for package_resource in self.package_list:
            package_folder = TelestoUtils.get_path_of_resource(package_resource)

            schema_path = os.path.join(package_folder, "schema.json")
            # check package can be loaded
            try:
                with open(schema_path) as f:
                    o = json.loads(f.read())
                    package_id = o["id"]

                self.logger.info(f"\tLoading package {package_resource} from {schema_path}")
            except:
                self.logger.error(f"\tUnable to load package {package_resource} from {schema_path}")
                sys.exit(0)
            self.package_folders[package_id] = package_folder
            self.packages[package_id] = {"package": package_resource}

        self.load_templates()

    def get_path(self):
        return self.workspace_path

    def get_resource_roots(self, from_roots={}):

        telesto_static_folder = TelestoUtils.get_path_of_resource("telesto.static")
        narvi_static_folder = TelestoUtils.get_path_of_resource("narvi.static")

        apps_common_folder = TelestoUtils.get_path_of_resource("telesto.apps.common")
        resource_roots = {}
        resource_roots[("static", "**")] = telesto_static_folder
        resource_roots["**/skadi-page.js"] = os.path.join(telesto_static_folder, "skadi", "skadi-page.js")
        resource_roots[("common", "topology_engine.js")] = apps_common_folder
        resource_roots[("common", "topology_store.js")] = apps_common_folder

        for package_id, package_folder in self.package_folders.items():
            resource_roots[(f"schema/{package_id}", "**")] = package_folder
        for (key,value) in from_roots.items():
            resource_roots[key] = value
        return resource_roots

    def get_platform_extensions(self):
        from hyrrokkin import __version__ as HYRROKKIN_VERSION
        from telesto import __version__ as TELESTO_VERSION
        from narvi import __version__ as NARVI_VERSION
        platform_extensions = []
        platform_extensions.append({"name": "Hyrrokkin", "version": HYRROKKIN_VERSION,
                                    "license_name": "MIT", "url": "https://codeberg.org/visual-topology/hyrrokkin"})
        platform_extensions.append({"name": "Narvi", "version": NARVI_VERSION,
                                    "license_name": "MIT", "url": "https://codeberg.org/visual-topology/narvi"})
        platform_extensions.append({"name": "Telesto", "version": TELESTO_VERSION,
                                    "license_name": "MIT", "url": "https://codeberg.org/visual-topology/telesto"})
        return platform_extensions

    def get_topology_statuses(self):
        service_statuses = self.server.get_service_statuses(self.workspace_id)
        runner_statuses = service_statuses.get("topology_runner", {}).get("instances", {})
        return runner_statuses

    def load_templates(self):
        for topology_id in self.templates:
            topology_folder = os.path.join(self.workspace_path, topology_id)
            if not os.path.exists(topology_folder):
                import_path = self.templates[topology_id]["import_path"]
                self.logger.info(f"loading {topology_id} from template {import_path}")
                TopologyDirectory.load_template(import_path, topology_folder)

    def bind(self, server):
        self.server = server
        package_urls = []
        for package_id in self.packages:
            package_urls.append(f"schema/{package_id}")

        applications = {}

        for app_name, app_config in self.applications.items():
            self.logger.info(f"registering application {app_name}")
            name = app_config.get("name")
            description = app_config.get("description", "")
            topology_id = app_config.get("topology_id", "")

            application_package = app_config.get("application_package")

            topology_path = os.path.join(self.workspace_path, topology_id, "topology.json")
            if not os.path.exists(topology_path):
                self.logger.error(
                    f"Application {app_name} configuration error, no topology found in {topology_path}")
                sys.exit(-1)

            application_runner = self.server.register_service(
               workspace=self.workspace_id,
               app_service_name=RUNNER_SERVICE_NAME,
               app_cls_name="telesto.app_services.topology_runner.TopologyRunner",
               app_parameters={
                   "packages": self.packages,
                   "workspace_path": self.workspace_path,
                   "hyrrokkin_options": self.hyrrokkin_options
               }, shared_service=False, fixed_service_id=topology_id,
               idle_timeout=0)

            application_resource_roots = self.get_resource_roots({
                "topology_application.js": TelestoUtils.get_path_of_resource("telesto.apps", "topology_application.js"),
                ("","*") : TelestoUtils.get_path_of_resource(application_package)
            })

            self.server.register_app(app_name=app_name,
                                     application_service=application_runner,
                                     app_parameters={
                                         "base_url": self.base_url,
                                         "package_urls": package_urls,
                                         "platform_extensions": self.get_platform_extensions(),
                                         "workspace_id": self.workspace_id,
                                         "topology_id": topology_id
                                     },
                                     resource_roots=application_resource_roots)

            applications[app_name] = {
                "name": name,
                "description": description,
                "url": f"{self.base_url}/{self.workspace_id}/{app_name}/index.html"
            }

        topology_runner = server.register_service(workspace=self.workspace_id, app_service_name=RUNNER_SERVICE_NAME,
                                                       app_cls_name="telesto.app_services.topology_runner.TopologyRunner",
                                                       app_parameters={
                                                           "packages": self.packages,
                                                           "workspace_path": self.workspace_path,
                                                           "hyrrokkin_options": self.hyrrokkin_options
                                                       }, shared_service=True,
                                                       service_id_validator=
                                                       lambda topology_id: os.path.exists(
                                                           os.path.join(self.workspace_path, topology_id)),
                                                       idle_timeout=self.idle_timeout)

        designer_resource_roots = self.get_resource_roots({
            "index.html": TelestoUtils.get_path_of_resource("telesto.apps", "topology_designer.html"),
            "topology_designer.js": TelestoUtils.get_path_of_resource("telesto.apps", "topology_designer.js")
        })

        self.server.register_app(app_name=DESIGNER_APP_NAME,
                                 application_service=topology_runner,
                                 app_parameters={
                                     "package_urls": package_urls,
                                     "topology": {},
                                     "read_only": False,
                                     "platform_extensions": self.get_platform_extensions(),
                                     "restartable": not self.hyrrokkin_options["in_process"],
                                     "skadi_options": self.skadi_options
                                 },
                                 resource_roots=designer_resource_roots,
                                 service_chooser_app_name=DIRECTORY_APP_NAME)

        directory_service = server.register_service(workspace=self.workspace_id,
                                                         app_cls_name="telesto.app_services.topology_directory.TopologyDirectory",
                                                         app_service_name="directory_service",
                                                         app_parameters={
                                                             "workspace_path": self.workspace_path,
                                                             "packages": self.packages,
                                                             "applications": applications,
                                                             "templates": self.templates,
                                                             "get_topology_statuses_callback": lambda: self.get_topology_statuses(),
                                                             "topology_update_callback": lambda action,
                                                                                                topology_id: self.topology_update(
                                                                 action, topology_id)
                                                         },
                                                         fixed_service_id="directory")

        directory_resource_roots = self.get_resource_roots({
            "index.html": TelestoUtils.get_path_of_resource("telesto.apps", "topology_directory.html"),
            "topology_directory.js": TelestoUtils.get_path_of_resource("telesto.apps", "topology_directory.js")
        })

        self.server.register_app(app_name=DIRECTORY_APP_NAME,
                                 application_service=directory_service,
                                 app_parameters={
                                     "designer_app_name": DESIGNER_APP_NAME,
                                     "base_url": self.base_url,
                                     "package_urls": package_urls,
                                     "skadi_options": self.skadi_options
                                 },
                                 resource_roots=directory_resource_roots)

        for topology_id in self.autostart:
            self.server.start_service(workspace=self.workspace_id,app_service_name=RUNNER_SERVICE_NAME,service_id=topology_id)

    def topology_update(self, action, topology_id):
        if action == "create":
            pass
        elif action == "reload":
            self.server.restart_service(self.workspace_id, RUNNER_SERVICE_NAME, topology_id)
        elif action == "remove":
            self.server.stop_service(self.workspace_id, RUNNER_SERVICE_NAME, topology_id)




