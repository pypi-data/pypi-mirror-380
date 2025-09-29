/*
 Telesto
 Copyright (C) 2025  Visual Topology Ltd

 MIT License

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
*/

var telesto = telesto || {};

telesto.TopologyEngine = class extends skadi.EngineBase {

    constructor(webapp, is_restartable) {
        super();
        this.webapp = webapp;
        this.skadi_api = null;
        this.pending_messages = [];
        this.is_restartable = is_restartable;
        this.load_callback = null;
        this.paused = false;
        this.client_services = {};
    }

    set_load_callback(callback) {
        this.load_callback = callback;
    }

    get_name() {
        return "telesto_engine";
    }

    restartable() {
        return this.is_restartable;
    }

    restart() {
        this.webapp.send({
            "action": "restart_execution"
        });
    }

    async load() {
    }

    async init() {
    }

    async bind(skadi_api) {
        this.skadi_api = skadi_api;
        super.bind(skadi_api);
        while(this.pending_messages.length > 0) {
            await this.handle(this.pending_messages.shift());
        }
    }

    async add_node(node_id, node_type_id, x, y, metadata, copy_from_node_id) {
        this.webapp.send({
            "action": "add_node",
            "node_id": node_id,
            "node_type": node_type_id,
            "x": x,
            "y": y,
            "metadata": metadata,
            "copy_from_node_id": copy_from_node_id
        });
    }

    async remove_node(node_id) {
        this.webapp.send({
            "action": "remove_node",
            "node_id": node_id
        });
    }

    async move_node(node_id, x, y) {
        this.webapp.send({
            "action": "move_node",
            "node_id": node_id,
            "x": x,
            "y": y
        });
    }

    async update_node_metadata(node_id, metadata) {
        this.webapp.send({
           "action": "update_node_metadata",
           "node_id": node_id,
           "metadata": metadata
        });
    }

    async add_link(link_id, link_type, from_node_id, from_port, to_node_id, to_port) {
        this.webapp.send({
            "action": "add_link",
            "link_id": link_id,
            "link_type": link_type,
            "from_node": from_node_id,
            "from_port": from_port,
            "to_node": to_node_id,
            "to_port": to_port
        });
    }

    async remove_link(link_id) {
        this.webapp.send({
            "action": "remove_link",
            "link_id": link_id
        });
    }

    async clear() {
        this.webapp.send({
            "action": "clear"
        });
    }

    update_design_metadata(updated_metadata) {
        this.webapp.send({
            "action": "update_design_metadata",
            "metadata": updated_metadata
        });
    }

    pause() {
        this.webapp.send({
            "action": "pause_execution"
        });
    }

    resume() {
        this.webapp.send({
            "action": "resume_execution"
        });
    }

    async handle(raw_msg) {
        if (this.skadi_api === null) {
            this.pending_messages.push(raw_msg);
            return null;
        }
        // Binary messages are always messages from a node or configuration to the page
        if (raw_msg instanceof ArrayBuffer) {
            // binary
            let dec_msg = hyrrokkin_engine.MessageUtils.decode_message(raw_msg);
            let msg_header = dec_msg[0];
            let content = dec_msg.slice(1);
            let action = msg_header["action"];
            if (action === "client_message") {
                let target_id = msg_header["target_id"];
                let target_type = msg_header["target_type"];
                let client_id = msg_header["client_id"];
                let key = this.get_client_key(target_id, target_type, client_id);
                if (key in this.client_services) {
                    this.client_services[key].send_message(...content);
                }
            }
        } else {
            let msg = JSON.parse(raw_msg);
            let handled = await this.handle_message(msg);
            if (!handled) {
                console.warn("message not handled: "+JSON.stringify(msg));
            }
        }
    }

    async handle_message(msg) {
        var action = msg["action"];
        if (action === "init") {
            if (this.webapp.set_download_url) {
                this.webapp.set_download_url(msg["download_url"]);
            }
            if (msg["topology"]) {
                await this.skadi_api.load(msg["topology"],{},true);
                if (this.load_callback) {
                    this.load_callback(this.skadi_api);
                }
             }
        } else if (action === "add_node") {
            let node_id = msg["node_id"];
            let node_type = msg["node_type"];
            let xc = msg["x"];
            let yc = msg["y"];
            let metadata = msg["metadata"];
            let copy_from_node_id = msg["copy_from_node_id"];
            this.skadi_api.add_node(node_id, node_type, xc, yc, metadata, this.event_handlers,copy_from_node_id);
        } else if (action === "move_node") {
            let node_id = msg["node_id"];
            let xc = msg["x"];
            let yc = msg["y"];
            this.skadi_api.move_node(node_id, xc, yc, this.event_handlers);
        } else if (action === "add_link") {
            let link_id = msg["link_id"]
            let link_type = msg["link_type"]
            let from_node_id = msg["from_node"]
            let from_port = msg["from_port"]
            let to_node_id = msg["to_node"]
            let to_port = msg["to_port"]
            this.skadi_api.add_link(link_id, link_type, from_node_id, from_port, to_node_id, to_port, this.event_handlers);
        } else if (action === "remove_node") {
            let node_id = msg["node_id"];
            this.skadi_api.remove_node(node_id, this.event_handlers);
        } else if (action === "remove_link") {
            let link_id = msg["link_id"];
            this.skadi_api.remove_link(link_id, this.event_handlers);
        } else if (action === "clear") {
            this.skadi_api.clear(true, this.event_handlers);
        } else if (action === "set_node_status") {
            let node_id = msg["node_id"];
            let status_msg = msg["status_message"];
            let status_state = msg["status_state"];
            this.skadi_api.set_node_status(node_id, status_msg, status_state);
        } else if (action === "set_node_execution_state") {
            let node_id = msg["node_id"];
            let execution_state = msg["execution_state"];
            this.skadi_api.update_execution_state(node_id, execution_state);
        } else if (action === "execution_complete") {
            this.skadi_api.execution_complete();
        } else if (action === "set_configuration_status") {
            let package_id = msg["package_id"];
            let status_msg = msg["status_message"];
            let status_state = msg["status_state"];
            this.skadi_api.set_configuration_status(package_id, status_msg, status_state);
        } else if (action === "open_client_request") {
            let target_id = msg["target_id"];
            let target_type = msg["target_type"];
            let client_name = msg["client_name"];
            this.skadi_api.request_open_client(target_id, target_type, client_name);
        } else {
            return false;
        }
        return true;
    }

    create_node_wrapper(core_node) {
        return new skadi.GraphWorkerWrapper(this, core_node, "node");
    }

    create_configuration_wrapper(core_configuration) {
        return new skadi.GraphWorkerWrapper(this, core_configuration, "configuration");
    }

    get_client_key(target_id, target_type, client_id) {
        return target_id + "/" + target_type + "/" + client_id;
    }

    open_client(target_id, target_type, client_id, client_options, client_service) {
        let key = this.get_client_key(target_id,target_type,client_id);
        this.client_services[key] = client_service;
        client_service.set_message_handler((...msg) => this.forward_client_message(target_id, target_type, client_id, ...msg));
        this.webapp.send({
            "action": "open_client",
            "target_id": target_id,
            "target_type": target_type,
            "client_id": client_id,
            "client_options": client_options
        });
    }

    forward_client_message(target_id, target_type, client_id, ...msg) {
        // message from a client, forward to the app
        let msg_header = {
            "action": "client_message",
            "client_id":client_id,
            "target_type":target_type,
            "target_id": target_id
        }
        let message_content = [msg_header].concat(msg);
        let enc_msg = hyrrokkin_engine.MessageUtils.encode_message(...message_content);
        this.webapp.send(enc_msg);
    }

    close_client(target_id, target_type, client_id) {
       this.webapp.send({
            "action": "close_client",
            "target_id": target_id,
            "target_type": target_type,
            "client_id": client_id
        });
        let key = this.get_client_key(target_id,target_type,client_id);
        if (key in this.client_services) {
            delete this.client_services[key];
        }
    }
}





