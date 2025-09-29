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

import logging
import argparse
import tomllib
import os
import signal
import sys

from telesto.api.telesto import Telesto

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--configuration", nargs="+", help="Specify the path(s) to configuration file(s) for each workspace", default=None)

    # these common options allow settings in the configuration file to be overridden
    parser.add_argument("--host", help="Specify the host name at which the service will listen", default="localhost")
    parser.add_argument("--port", type=int, help="Specify the port number at which the service will listen", default=8889)
    parser.add_argument("--base-url", help="Specify the base url at which the service will listen", default="")

    parser.add_argument("--launch-ui", type=str, help="Desktop mode: specify a command launch a web browser on startup, for example \"chromium --app=URL\".  URL will be substituted for the url of the first workspace's directory. ", default="")
    parser.add_argument("--verbose", action="store_true", help="enable verbose logging", default=None)
    parser.add_argument("--in-process", action="store_true", help="ask to run engines in-process", default=None)
    parser.add_argument("--use-server", choices=["auto","tornado","builtin"], help="Choose which web-server to use", default="auto")

    parser.add_argument("--generate-example-configuration", type=str, metavar="PATH",
                        help="Generate a sample workspace configuration file to this path and then exit", default=None)

    parser.add_argument("--include-packages", nargs="+", type=str, metavar="PACKAGE",
                        help="Add these packages to each workspace", default=[])

    parser.add_argument("--exclude-packages", nargs="+", type=str, metavar="PATTERN",
                        help="Exclude packages matching this pattern (use * as a wildcard) from each workspace", default=[])

    parser.add_argument("--workspace-root-folder", type=str, metavar="PATH",
                        help="Specify a root folder for workspaces", default=None)

    parser.add_argument("--main-workspace-id", type=str, metavar="WORKSPACE_ID",
                        help="If multiple workspaces are defined, specify a main one", default=None)



    parser.add_argument("--monitoring", nargs=2, type=int, metavar=("INTERVAL_S","RETENTION_S"), help="Enable narvi service monitoring with the specified interval and retention period (in seconds) set either to zero to disable monitoring", default=(0,0))

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if args.generate_example_configuration:
        with open(os.path.join(os.path.split(__file__)[0], "telesto_defaults.toml")) as f:
            contents = f.read()
            with open(args.generate_example_configuration) as of:
                of.write(contents)
        sys.exit(0)
    else:
        if args.configuration:
            configuration_paths = args.configuration
        else:
            configuration_paths = [os.path.join(os.path.split(__file__)[0], "telesto_defaults.toml")]

        workspace_configs = []
        for configuration_path in configuration_paths:
            with open(configuration_path) as f:
                workspace_configs.append(tomllib.loads(f.read()))

        app = Telesto(configurations=workspace_configs, workspace_root_folder=args.workspace_root_folder,
                      host=args.host, port=args.port, base_url=args.base_url, launch_ui=args.launch_ui,
                      include_packages=args.include_packages, exclude_packages=args.exclude_packages,
                      monitoring=args.monitoring, main_workspace_id=args.main_workspace_id,
                      in_process=args.in_process, use_server=args.use_server)
        app.run()


if __name__ == '__main__':
    main()