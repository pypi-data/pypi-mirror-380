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

from typing import Callable
import uuid
import threading
import logging
import os

from .client import Client
from hyrrokkin.execution_manager.execution_manager import ExecutionManager

from hyrrokkin.execution_manager.execution_client import ExecutionClient
from hyrrokkin.engine_launchers.engine_launcher import EngineLauncher
from hyrrokkin.engine_launchers.javascript_engine_launcher import JavascriptEngineLauncher
from hyrrokkin.engine_launchers.python_engine_launcher import PythonEngineLauncher

def threadsafe(func):
    """
    Decorator that serialises access to a methods from multiple threads
    :param func: the method to be decorated
    :return: wrapped method
    """
    def threadsafe_wrapper(self, *args, **kwargs):
        try:
            self.lock.acquire()
            return func(self, *args, **kwargs)
        finally:
            self.lock.release()
    return threadsafe_wrapper

def check_closed(func):
    """
    Decorator that prevents access to a method once the closed attribute is set to True
    :param func: the method to be decorated
    :return: wrapped method
    """
    def threadsafe_wrapper(self, *args, **kwargs):
        if self.closed:
            raise Exception("Runner is closed")
        return func(self, *args, **kwargs)
    return threadsafe_wrapper

class TopologyRunner:

    def __init__(self, network, schema, execution_folder, engine_launcher, status_event_handler, execution_event_handler, read_only):

        self.network = network
        self.schema = schema
        self.execution_folder = execution_folder
        self.engine_launcher = engine_launcher
        self.status_event_handler = status_event_handler
        self.execution_event_handler = execution_event_handler
        self.read_only = read_only
        self.injected_inputs = {}
        self.output_listeners = {}

        self.closed = False
        self.close_handler = None

        self.logger = logging.getLogger("topology_runner")

        self.add_node_callback = None
        self.add_link_callback = None
        self.remove_node_callback = None
        self.remove_link_callback = None
        self.clear_network_callback = None

        if self.engine_launcher is None:
            # try to work out which engine to run
            for candidate_launcher in [PythonEngineLauncher(), JavascriptEngineLauncher()]:
                valid = True
                for package_id in schema.get_packages():
                    folder = schema.get_package_path(package_id)
                    if not os.path.exists(os.path.join(folder, candidate_launcher.get_configuration_filename())):
                        valid = False
                if valid:
                    self.engine_launcher = candidate_launcher
                    break

        self.paused = False

        self.lock = threading.RLock()
        self.thread = None

        for (package_id, package) in self.schema.get_packages().items():
            self.engine_launcher.configure_package(package_id, self.schema.get_package_resource(package_id), self.schema.get_package_path(package_id))

        self.execution_clients = {}

        self.session_ids = set()

        self.create_executor()


    def create_executor(self):
        self.executor = ExecutionManager(self.schema,
                                         execution_folder=self.execution_folder,
                                         status_callback=self.status_event_handler,
                                         node_execution_callback=self.execution_event_handler,
                                         engine_launcher=self.engine_launcher,
                                         read_only=self.read_only,
                                         client_message_handler=lambda *args: self.__handle_client_message(*args),
                                         properties_update_handler=lambda target_id, target_type, properties:
                                            self.__handle_properties_update(target_id, target_type, properties),
                                         data_update_handler=lambda target_id, target_type, key, value:
                                            self.__handle_data_update(target_id, target_type, key, value))

        self.executor.set_request_open_client_callback(lambda origin_id, origin_type, session_id, client_name: self.__request_open_client(origin_id, origin_type, session_id, client_name))

        self.open_client_request_handler = None

        self.execution_result = None

        self.executor.init()

        if self.executor.engine_launcher.get_persistence() != "shared_filesystem":
            for package_id in self.schema.get_packages():
                dsu = self.network.get_configuration_datastore(package_id)
                self.executor.load_target(package_id, "configuration", dsu)

        for (package_id, package) in self.schema.get_packages().items():
            self.executor.add_package(package_id, package.get_schema(),
                                      self.schema.get_package_path(package_id))

        if self.executor.engine_launcher.get_persistence() != "shared_filesystem":
            for node_id in self.network.get_node_ids():
                dsu = self.network.get_node_datastore(node_id)
                self.executor.load_target(node_id, "node", dsu)

        # load all nodes and links into the execution

        for node_id in self.network.get_node_ids():
            self.executor.add_node(self.network.get_node(node_id), copy_from_node_id="")

        for link_id in self.network.get_link_ids():
            self.executor.add_link(self.network.get_link(link_id))

        # listen for further network changes and update the execution accordingly

        self.add_node_callback = self.network.register_add_node_callback(lambda node, copy_from_node_id: self.__add_node(node, copy_from_node_id))
        self.reset_node_callback = self.network.register_reset_node_callback(lambda node: self.__reset_node(node))

        self.add_link_callback = self.network.register_add_link_callback(lambda link: self.__add_link(link))

        self.remove_node_callback = self.network.register_remove_node_callback(
            lambda node: self.__remove_node(node))
        self.remove_link_callback = self.network.register_remove_link_callback(
            lambda link: self.__remove_link(link))

        self.clear_network_callback = self.network.register_clear_network_callback(lambda: self.__clear())

        for session_id in self.session_ids:
            self.executor.open_session(session_id)

        for (target_id, target_type, session_id, client_id) in self.execution_clients:
            client = self.execution_clients[(target_id, target_type, session_id, client_id)]
            self.executor.connect_client(target_id, target_type, session_id, client_id, client)

        for ((node_id, output_port_name),listener) in self.output_listeners.items():
            self.executor.add_output_listener(node_id, output_port_name, listener)

        for ((node_id, input_port_name),value) in self.injected_inputs.items():
            self.executor.inject_input_value(node_id, input_port_name, value)

    @check_closed
    @threadsafe
    def inject_input_value(self, node_id:str, input_port_name:str, value:bytes):
        """
        Inject input values into a node in the topology.

        Args:
            node_id: the node id
            input_port_name: the name of the node's input port
            value: the value to inject - encoded as bytes
        """
        self.injected_inputs[(node_id, input_port_name)] = value
        self.executor.inject_input_value(node_id, input_port_name, value)

    @check_closed
    @threadsafe
    def add_output_listener(self, node_id:str, output_port_name:str, listener:Callable[[bytes], None]):
        """
        Listen for values output from a node in the topology.  Replaces any existing listener on the node/port if present.

        Args:
            node_id: the node id
            output_port_name: the name of the node's output port
            listener: a callback function which is invoked with the value on the output port when the node is run
        """
        self.output_listeners[(node_id, output_port_name)] = listener
        self.executor.add_output_listener(node_id, output_port_name, listener)

    @check_closed
    @threadsafe
    def remove_output_listener(self, node_id:str, output_port_name:str):
        """
        Remove a listener from a node/port

        Args:
            node_id: the node id
            output_port_name: the name of the node's output port
        """
        self.executor.remove_output_listener(node_id, output_port_name)

    @check_closed
    @threadsafe
    def open_session(self, session_id:str|None=None) -> str:
        """
        Open a new session

        Args:
            session_id: the identifier of the session or None to generate a new session identifier

        Returns:
            the session identifier for the opened session
        """

        if not session_id:
            session_id = str(uuid.uuid4())

        if session_id not in self.session_ids:
            self.session_ids.add(session_id)
            self.executor.open_session(session_id)
        else:
            self.logger.warning(f"open_session: session {session_id} is already open")

        return session_id

    @check_closed
    @threadsafe
    def close_session(self, session_id:str):
        """
        Close a session

        Args:
            session_id: the identifier of the session to close
        """
        if session_id in self.session_ids:
            self.session_ids.remove(session_id)
            self.executor.close_session(session_id)
        else:
            self.logger.warning(f"open_session: session {session_id} is already open")


    @check_closed
    @threadsafe
    def set_request_open_client_callback(self, open_client_request_handler: Callable[[str,str,str,str],None]):
        """
        Attach a function that will be called when a node requests that a client be attached

        Args:
            open_client_request_handler: function that is called with the origin_id, origin_type, session_id, client_name as parameters
        """
        self.open_client_request_handler = open_client_request_handler

    @check_closed
    @threadsafe
    def set_execution_complete_callback(self, execution_complete_callback: Callable[[], None]):
        """
        Attach a function that will be called whenever execution of the topology completes

        Args:
            execution_complete_callback: function that will be called
        """
        self.executor.set_execution_complete_callback(execution_complete_callback)

    @check_closed
    @threadsafe
    def attach_node_client(self, node_id: str, session_id: str="", client_id: str="", client_options: dict = {}) -> Client:
        """
        Attach a client instance to a node.  Any client already attached to the node with the same client_id
        will be detached.

        Args:
            node_id: the node to which the client is to be attached
            session_id: the id of an opened interactive session
            client_id: the name of the client to attach, as defined in the node's schema
            client_options: optional, a dictionary with extra parameters from the client

        Returns:
             an object which implements the Client API and provides methods to interact with the client

        """
        if not session_id or session_id not in self.session_ids:
            session_id = self.open_session(session_id)
        client = Client(session_id)
        execution_client = ExecutionClient(lambda *args: self.__forward_client_message(*args),
                                           node_id, "node", session_id, client_id, client,
                                           client_options)
        self.execution_clients[(node_id, "node", session_id, client_id)] = execution_client
        self.executor.attach_client(node_id, "node", session_id, client_id, execution_client)
        return client

    @check_closed
    @threadsafe
    def detach_node_client(self, node_id: str, session_id:str, client_id: str):
        """
        Detach a client instance from a node

        Args:
            node_id: the node to which the client is to be attached
            session_id: the id of an opened interactive session
            client_id: the id of the client to detach
        """
        if (node_id, "node", session_id, client_id) in self.execution_clients:
            client = self.execution_clients[(node_id, "node", session_id, client_id)]
            self.executor.detach_client(node_id, "node", session_id, client_id, client)
            del self.execution_clients[(node_id, "node", session_id, client_id)]

    @check_closed
    @threadsafe
    def attach_configuration_client(self, package_id: str, session_id:str = "", client_id:str = "", client_options: dict = {}) -> Client:
        """
        Attach a client instance to a package configuration

        Args:
            package_id: the package configuration to which the client is to be attached
            session_id: the id of an opened interactive session
            client_id: the id of the client to attach
            client_options: optional, a dictionary with extra parameters for the client

        Returns:
             an object which implements the Client API and provides methods to interact with the client
        """
        if not session_id or session_id not in self.session_ids:
            session_id = self.open_session(session_id)
        client = Client(session_id)
        execution_client = ExecutionClient(lambda *args: self.__forward_client_message(*args),
                                           package_id, "configuration", session_id, client_id, client, client_options)
        self.execution_clients[(package_id, "configuration", session_id, client_id)] = execution_client
        self.executor.attach_client(package_id, "configuration", session_id, client_id, execution_client)
        return client

    @check_closed
    @threadsafe
    def detach_configuration_client(self, package_id: str, session_id: str, client_id):
        """
        Detach a client instance from a package configuration

        Args:
            package_id: the node to which the client is to be attached
            session_id: the id of an opened interactive session
            client_id: the id of the client to detach
        """
        if (package_id, "configuration", session_id, client_id) in self.execution_clients:
            client = self.execution_clients[(package_id, "configuration", session_id, client_id)]
            self.executor.detach_client(package_id, "configuration", session_id, client_id, client)
            client.close()
            del self.execution_clients[(package_id, "configuration", session_id, client_id)]

    def __handle_client_message(self, target_id, target_type, session_id, client_id, extras):
        if (target_id, target_type, session_id, client_id) in self.execution_clients:
            client = self.execution_clients[(target_id, target_type, session_id, client_id)]
            client.message_callback(*extras)

    def __handle_properties_update(self, target_id, target_type, properties):
        if target_type == "configuration":
            dsu = self.network.get_configuration_datastore(target_id)
        else:
            dsu = self.network.get_node_datastore(target_id)
        dsu.set_properties(properties)

    def __handle_data_update(self, target_id, target_type, key, value):
        if target_type == "configuration":
            dsu = self.network.get_configuration_datastore(target_id)
        else:
            dsu = self.network.get_node_datastore(target_id)
        dsu.set_data(key, value)

    @threadsafe
    def __forward_client_message(self, target_id, target_type, session_id, client_id, *msg):
        self.executor.forward_client_message(target_id, target_type, session_id, client_id, *msg)

    @threadsafe
    def __add_node(self, node, copy_from_node_id):
        self.executor.add_node(node, copy_from_node_id)

    @threadsafe
    def __reset_node(self, node):
        self.executor.reset_node(node)

    @threadsafe
    def __add_link(self, link):
        self.executor.add_link(link)

    @threadsafe
    def __remove_node(self, node):
        self.executor.remove_node(node.get_node_id())

    @threadsafe
    def __remove_link(self, link):
        self.executor.remove_link(link.get_link_id())

    @threadsafe
    def __clear(self):
        self.executor.clear()

    @threadsafe
    def pause(self):
        """
        Pause execution of the topology.  Until resume is called, no nodes will start running.
        """
        self.paused = True
        self.executor.pause()

    @check_closed
    @threadsafe
    def resume(self, after_message_delivery:bool=False):
        """
        Resume execution of the topology

        Args:
            after_message_delivery: wait for all in-flight messages to be received by nodes and configurations before resuming
        """
        self.paused = False
        self.executor.resume(after_message_delivery=after_message_delivery)

    @check_closed
    @threadsafe
    def get_engine_pid(self):
        """
        Get the integer process identifier (PID) of the engine sub-process (or None if the engine is not running in a sub-process)

        Returns:
            engine PID
        """
        return self.executor.get_engine_pid()

    @check_closed
    @threadsafe
    def is_restartable(self):
        return self.executor.can_cancel()

    @check_closed
    @threadsafe
    def restart(self):
        """
        Restart execution of the topology, by cancelling and then creating a new executor
        """
        self.executor.cancel()
        self.executor = None
        self.create_executor()

    def start(self, terminate_on_complete=True, after_message_delivery=True):
        if self.thread is None:
            self.thread = threading.Thread(target=lambda: self.run(terminate_on_complete=terminate_on_complete,
                                                    after_message_delivery=after_message_delivery), daemon=True)
            self.thread.start()

    def join(self):
        self.thread.join()
        self.thread = None

    @check_closed
    def run(self, terminate_on_complete:bool=True, after_message_delivery:bool=True) -> bool:
        """
        Run the execution

        Args:
            terminate_on_complete: if true, terminate the runner as soon as all nodes have finished running
            after_message_delivery: if true, wait for all messages to be delivered to nodes/configurations before running

        Returns:
            True iff the execution resulted in no failed nodes
        """

        try:
            self.lock.acquire()
            self.executor.resume(after_message_delivery)
        finally:
            self.lock.release()
        self.execution_result = self.executor.run(terminate_on_complete=terminate_on_complete)

        return self.execution_result


    def set_close_callback(self, callback):
        self.close_handler = callback

    def get_result(self):
        return self.execution_result

    def get_failures(self):
        return self.executor.get_failures()

    @threadsafe
    @check_closed
    def stop(self) -> None:
        """
        Stop the current execution, callable from another thread during the execution of run

        Notes:
            the run method will return once any current node executions complete
        """
        if self.executor:
            self.executor.stop()


    @check_closed
    def close(self) -> None:
        """
        Close the runner.  After this call returns, no other methods can be called

        :return:
        """
        if self.executor:
            self.executor.close()
            self.executor = None

        # disconnect listeners from the network
        self.add_node_callback = self.network.unregister_add_node_callback(self.add_node_callback)
        self.reset_node_callback = self.network.unregister_reset_node_callback(self.reset_node_callback)
        self.add_link_callback = self.network.unregister_add_link_callback(self.add_link_callback)
        self.remove_node_callback = self.network.unregister_remove_node_callback(self.remove_node_callback)
        self.remove_link_callback = self.network.unregister_remove_link_callback(self.remove_link_callback)
        self.clear_network_callback = self.network.unregister_clear_network_callback(
            self.clear_network_callback)

        self.closed = True

        if self.close_handler:
            self.close_handler()


    def __request_open_client(self, origin_id, origin_type, session_id, client_id):
        """
        Pass on a request to open a node or configuration client

        Args:
            origin_id:
            origin_type:
            session_id:
            client_id:

        Returns:

        """
        if self.open_client_request_handler is not None:
            self.open_client_request_handler(origin_id, origin_type, session_id, client_id)
