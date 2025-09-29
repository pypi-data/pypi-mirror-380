#   Hyrrokkin - a library for building and running executable graphs
#
#   MIT License - Copyright (C) 2022-2025  Visual Topology Ltd
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#   and associated documentation files (the "Software"), to deal in the Software without
#   restriction, including without limitation the rights to use, copy, modify, merge, publish,
#   distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all copies or
#   substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
#   BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#   DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import socket

import logging

from .process_runner import ProcessRunner
from .thread_runner import ThreadRunner

from hyrrokkin_engine.message_utils import MessageUtils
from ..engine_launchers.engine_launcher import EngineLauncher


class ExecutionManager:

    def __init__(self, schema, execution_folder=None, status_callback=None, node_execution_callback=None,
                 engine_launcher=None, read_only=False, client_message_handler=None, properties_update_handler=None,
                 data_update_handler=None):
        self.schema = schema
        self.execution_folder=execution_folder
        self.stop_on_execution_complete = False
        self.status_callback = status_callback
        self.node_execution_callback = node_execution_callback
        self.read_only = read_only
        self.execution_complete_callback = None
        self.injected_inputs = {}
        self.output_listeners = {}
        self.host_name = "localhost"
        self.engine_pid = None
        self.listening_sock = None
        self.connected = False
        self.msg_handler = None
        self.port = None
        self.count_failed = 0
        self.failures = {}
        self.running = False
        self.terminate_on_complete = False
        self.logger = logging.getLogger("execution_manager")
        self.engine_launcher = engine_launcher
        self.restarting = False
        self.request_open_client_callback = None
        self.client_message_handler = client_message_handler
        self.worker_closed = False
        self.properties_update_handler = properties_update_handler
        self.data_update_handler = data_update_handler

    def inject_input_value(self, node_id, input_port_name, injected_value):
        self.send_message({
            "action": "inject_input",
            "node_id": node_id,
            "input_port_name": input_port_name
        }, injected_value)

    def add_output_listener(self, node_id, output_port_name, listener):
        if listener is not None:
            if node_id not in self.output_listeners:
                self.output_listeners[node_id] = {}
            self.output_listeners[node_id][output_port_name] = listener
            self.send_message({
                "action": "add_output_listener",
                "node_id": node_id,
                "output_port_name": output_port_name
            })

    def remove_output_listener(self, node_id, output_port_name):
        if node_id in self.output_listeners:
            if output_port_name in self.output_listeners[node_id]:
                del self.output_listeners[node_id][output_port_name]
                self.send_message({
                    "action": "remove_output_listener",
                    "node_id": node_id,
                    "output_port_name": output_port_name
                })

    # notifications from execution

    def status_update(self, target_id, target_type, message, status):
        if self.status_callback:
            self.status_callback(target_id, target_type, message, status)
        return False

    def node_execution_update(self, at_time, node_id, node_execution_state, exn, is_manual):
        if self.node_execution_callback:
            self.node_execution_callback(at_time, node_id, node_execution_state, exn, is_manual)
        return False

    def set_execution_complete_callback(self, execution_complete_callback):
        self.execution_complete_callback = execution_complete_callback

    def set_request_open_client_callback(self, request_open_client_callback):
        self.request_open_client_callback = request_open_client_callback

    def execution_complete_update(self):
        if self.execution_complete_callback:
            self.execution_complete_callback()
        return self.stop_on_execution_complete

    def __start_remote_graph_process(self):
        args = self.engine_launcher.get_commandline(self.host_name, self.port)
        runner = ProcessRunner(args)
        self.engine_pid = runner.get_pid()
        runner.set_output_callback(lambda output: self.logger.info(f"[{self.engine_pid}] {output}"))
        runner.daemon = True
        runner.start()
        for input in self.engine_launcher.get_inputs():
            runner.send_input(input)
        runner.close_input()
        return runner

    def __start_local_graph_thread(self, verbose):
        runner = ThreadRunner(self.host_name, self.port, verbose)
        runner.start()
        return runner

    def serialise_injected_inputs(self):
        ser = []
        for (node_id,input_port) in self.injected_inputs:
            ser.append([node_id,input_port,self.injected_inputs[(node_id,input_port)]])
        return ser

    def serialise_output_listeners(self):
        ser = []
        for (node_id,output_port) in self.output_listeners:
            ser.append([node_id,output_port])
        return ser

    def init(self):

        self.listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listening_sock.bind((self.host_name,0))
        _, self.port = self.listening_sock.getsockname()
        self.listening_sock.listen(5)
        self.logger = logging.getLogger("execution_worker")

        self.start_runner()

    def start_runner(self):

        if self.engine_launcher.is_in_process():
            self.runner = self.__start_local_graph_thread(self.engine_launcher.verbose)
        else:
            self.runner = self.__start_remote_graph_process()

        self.sock, self.cliaddr = self.listening_sock.accept()

        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        init_msg = {
            "action": "init",
            "worker_configuration": self.engine_launcher.get_worker_configuration(),
            "read_only": self.read_only,
            "persistence_mode": self.engine_launcher.get_persistence(),
            "injected_inputs": self.serialise_injected_inputs(),
            "output_listeners": self.serialise_output_listeners()
        }

        if self.engine_launcher.get_persistence() == "shared_filesystem":
            init_msg["execution_folder"] = self.execution_folder

        self.send_message(init_msg)

    def run(self, terminate_on_complete=True):
        self.terminate_on_complete = terminate_on_complete
        self.running = True
        self.count_failed = 0
        self.failures = {}
        while self.running:
            msg = self.receive_message()
            if msg is None:
                break
            try:
                self.handle_message(msg)
            except:
                self.logger.exception("handle_message")
        return self.count_failed == 0

    def get_failures(self):
        return self.failures

    def get_engine_pid(self):
        return self.engine_pid

    def close(self):
        self.close_worker()
        self.sock.close()
        self.listening_sock.close()
        self.runner.join()

    def open_session(self, session_id):
        self.send_message({
            "action": "open_session",
            "session_id": session_id
        })

    def close_session(self, session_id):
        self.send_message({
            "action": "close_session",
            "session_id": session_id
        })

    def send_message(self, *message_parts):
        message_length = -1
        try:
            message_bytes = MessageUtils.encode_message(*message_parts)
            message_length = len(message_bytes)
            self.sock.send(len(message_bytes).to_bytes(4, "big"))
            sent = 0
            while sent < message_length:
                sent += self.sock.send(message_bytes[sent:])
            return True
        except:
            self.logger.exception(f"send message len={message_length}")
            return False

    def receive_message(self):
        message_length = -1
        try:
            message_length_bytes = self.sock.recv(4)
            message_length = int.from_bytes(message_length_bytes, "big")
            if message_length == 0:
                return None
            message_bytes = b''
            while len(message_bytes) < message_length:
                message_bytes += self.sock.recv(message_length-len(message_bytes))
            try:
                message_parts = MessageUtils.decode_message(message_bytes)
            except:
                self.logger.exception(f"decode message len={message_length}")
                return None
        except Exception:
            self.logger.exception(f"receive message len={message_length}")
            return None
        return message_parts


    def handle_client_message(self, target_id, target_type, session_id, client_id, extras):
        if self.client_message_handler:
            self.client_message_handler(target_id, target_type, session_id, client_id, extras)
        return True

    def forward_client_message(self, target_id, target_type, session_id, client_id, *msg):
        control_packet = {
            "action": "client_message",
            "target_id": target_id,
            "target_type": target_type,
            "session_id": session_id,
            "client_id": client_id
        }
        self.send_message(control_packet, *msg)

    def connect_client(self, target_id, target_type, session_id, client_id, execution_client):
        self.open_client(target_id, target_type, session_id, client_id, execution_client.get_client_options())
        execution_client.set_connected()

    def open_client(self, target_id, target_type, session_id, client_id, client_options):
        self.send_message({
            "action": "open_client",
            "target_id": target_id,
            "target_type": target_type,
            "session_id": session_id,
            "client_id": client_id,
            "client_options": client_options
        })

    def close_client(self, target_id, target_type, session_id, client_id):
        self.send_message({
            "action": "close_client",
            "target_id": target_id,
            "target_type": target_type,
            "session_id": session_id,
            "client_id": client_id
        })

    def handle_message(self, message_parts):
        control_packet = message_parts[0]
        action = control_packet["action"]
        match action:
            case "client_message":
                origin_id = control_packet["origin_id"]
                origin_type = control_packet["origin_type"]
                session_id = control_packet["session_id"]
                client_id = control_packet["client_id"]
                self.handle_client_message(origin_id, origin_type, session_id, client_id, message_parts[1:])
            case "update_execution_state":
                self.node_execution_update(control_packet.get("at_time",None), control_packet["node_id"],
                                       control_packet["execution_state"], control_packet.get("exn",None),
                                        control_packet["is_manual"])
            case "execution_started":
                pass
            case "execution_complete":
                self.count_failed = control_packet["count_failed"]
                self.failures = control_packet.get("failures",{})
                self.execution_complete_update()
                if self.terminate_on_complete:
                    self.running = False
            case "output_notification":
                self.notify_output(control_packet["node_id"],control_packet["output_port_name"],message_parts[1])
            case "update_status":
                self.status_update(control_packet["origin_id"],control_packet["origin_type"],control_packet["message"],control_packet["status"])
            case "request_open_client":
                self.request_open_client(control_packet["origin_id"], control_packet["origin_type"], control_packet.get("session_id",None), control_packet["client_name"])
            case "init_complete":
                pass
            case "set_properties":
                self.set_properties(control_packet["target_id"], control_packet["target_type"],control_packet["properties"])
            case "set_data":
                self.set_data(control_packet["target_id"], control_packet["target_type"],
                                control_packet["key"], message_parts[1])
            case _:
                self.logger.warning(f"Unhandled action {action}")

    def notify_output(self, node_id, output_port, value):
        if node_id in self.output_listeners:
            if output_port in self.output_listeners[node_id]:
                self.output_listeners[node_id][output_port](value)

    def stop(self):
        self.close_worker()

    def pause(self):
        self.send_message({
            "action": "pause"
        })

    def resume(self, after_message_delivery=False):
        self.send_message({
            "action": "resume",
            "after_message_delivery": after_message_delivery
        })

    def can_cancel(self):
        return not self.engine_launcher.is_in_process()

    def cancel(self):
        self.runner.stop(True)
        self.sock.close()
        self.listening_sock.close()
        self.runner.join()

    def attach_client(self, target_id, target_type, session_id, client_id, client):
        self.connect_client(target_id, target_type, session_id, client_id, client)

    def detach_client(self, target_id, target_type, session_id, client_id, client):
        client.disconnect()
        self.close_client(target_id, target_type, session_id, client_id)

    def close_worker(self):
        if not self.worker_closed:
            self.send_message({"action": "close"})
            self.worker_closed = True

    def add_node(self, node, copy_from_node_id=""):
        self.send_message({
            "action": "add_node",
            "node_id": node.get_node_id(),
            "node_type_id": node.get_node_type(),
            "copy_from_node_id": copy_from_node_id
        })



    def reset_node(self, node):
        self.send_message({
            "action": "reset_node",
            "node_id": node.get_node_id()
        })

    def add_link(self, link):
        self.send_message({
            "action": "add_link",
            "link_id": link.get_link_id(),
            "link_type": link.get_link_type(),
            "from_node_id": link.from_node_id,
            "from_port": link.from_port,
            "to_node_id": link.to_node_id,
            "to_port": link.to_port
        })

    def add_package(self, package_id, package_schema, package_folder):
        self.send_message({
            "action": "add_package",
            "package_id": package_id,
            "schema": package_schema,
            "folder": "file://"+package_folder
        })

    def load_target(self, target_id, target_type, persistence):

        self.send_message({
            "action": "set_properties",
            "target_id": target_id,
            "target_type": target_type,
            "properties": persistence.get_properties()
        })

        for key in persistence.get_data_keys():
            self.send_message({
                "action": "set_data",
                "target_id": target_id,
                "target_type": target_type,
                "key": key
            }, persistence.get_data(key))

    def set_properties(self, target_id, target_type, properties):
        if self.properties_update_handler:
            self.properties_update_handler(target_id, target_type, properties)

    def set_data(self, target_id, target_type, key, value):
        if self.data_update_handler:
            self.data_update_handler(target_id, target_type, key, value)

    def remove_node(self, node_id):
        self.send_message({
            "action": "remove_node",
            "node_id": node_id
        })

    def remove_link(self, link_id):
        self.send_message({
            "action": "remove_link",
            "link_id": link_id
        })

    def clear(self):
        self.send_message({
            "action": "clear"
        })

    def request_open_client(self, origin_id, origin_type, session_id, client_name):
        if self.request_open_client_callback:
            self.request_open_client_callback(origin_id, origin_type, session_id, client_name)














