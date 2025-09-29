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

import logging
import os.path
import uuid
from copy import deepcopy
import zipfile
import json
import io
import shutil

from hyrrokkin.model.node import Node as Node
from hyrrokkin.model.link import Link as Link
from hyrrokkin.utils.persistence_filesystem_sync import PersistenceFileSystemSync
from hyrrokkin.utils.persistence_memory_sync import PersistenceMemorySync

class Network:

    def __init__(self, schema, savedir):
        self.schema = schema
        self.savedir = savedir
        self.nodes = {}
        self.links = {}
        self.metadata = {}
        self.logger = logging.getLogger("network")
        self.add_node_callbacks = []
        self.reset_node_callbacks = []
        self.add_link_callbacks = []
        self.remove_node_callbacks = []
        self.remove_link_callbacks = []
        self.clear_network_callbacks = []
        self.node_datastores = {}
        self.configuration_datastores = {}
        for package_id in self.schema.get_packages():
            self.create_configuration_datastore(package_id)

    def create_node_datastore(self, node_id, copy_from_node_id=""):
        if self.savedir:
            p = PersistenceFileSystemSync(node_id,"node",self.savedir, False)
        else:
            p = PersistenceMemorySync()
        if copy_from_node_id:
            source_datastore = self.get_node_datastore(copy_from_node_id)
            p.set_properties(source_datastore.get_properties())
            for key in source_datastore.get_data_keys():
                p.set_data(key,source_datastore.get_data(key))
        self.node_datastores[node_id] = p

    def get_node_datastore(self, node_id):
        if node_id not in self.node_datastores:
            self.create_node_datastore(node_id)
        return self.node_datastores[node_id]

    def create_configuration_datastore(self, package_id):
        if self.savedir:
            p = PersistenceFileSystemSync(package_id, "configuration", self.savedir, False)
        else:
            p = PersistenceMemorySync()
        self.configuration_datastores[package_id] = p

    def get_configuration_datastore(self, package_id):
        if package_id not in self.configuration_datastores:
            self.create_configuration_datastore(package_id)
        return self.configuration_datastores[package_id]

    def register_add_node_callback(self, callback):
        self.add_node_callbacks.append(callback)
        return callback

    def register_reset_node_callback(self, callback):
        self.reset_node_callbacks.append(callback)
        return callback

    def register_add_link_callback(self, callback):
        self.add_link_callbacks.append(callback)
        return callback

    def register_remove_node_callback(self, callback):
        self.remove_node_callbacks.append(callback)
        return callback

    def register_remove_link_callback(self, callback):
        self.remove_link_callbacks.append(callback)
        return callback

    def register_clear_network_callback(self, callback):
        self.clear_network_callbacks.append(callback)
        return callback

    def unregister_add_node_callback(self, callback):
        if callback is not None:
            self.add_node_callbacks.remove(callback)
        return None

    def unregister_reset_node_callback(self, callback):
        if callback is not None:
            self.reset_node_callbacks.remove(callback)
        return None

    def unregister_add_link_callback(self, callback):
        if callback is not None:
            self.add_link_callbacks.remove(callback)
        return None

    def unregister_remove_node_callback(self, callback):
        if callback is not None:
            self.remove_node_callbacks.remove(callback)
        return None

    def unregister_remove_link_callback(self, callback):
        if callback is not None:
            self.remove_link_callbacks.remove(callback)
        return None

    def unregister_clear_network_callback(self, callback):
        if callback is not None:
            self.clear_network_callbacks.remove(callback)
        return None

    def get_directory(self):
        return self.savedir

    def get_schema(self):
        return self.schema

    def add_node(self, node, loading=False, copy_from_node_id=""):
        node_id = node.get_node_id()
        self.nodes[node_id] = node
        self.create_node_datastore(node_id, copy_from_node_id=copy_from_node_id)
        if not loading:
            self.__save_dir()
        for callback in self.add_node_callbacks:
            callback(node, copy_from_node_id)

    def reset_node(self, node):
        for callback in self.reset_node_callbacks:
            callback(node)

    def move_node(self, node_id, x, y):
        self.nodes[node_id].move_to(x, y)
        self.__save_dir()

    def get_node(self, node_id):
        return self.nodes.get(node_id, None)

    def get_node_ids(self, traversal_order=None):
        if traversal_order is None:
            return list(self.nodes.keys())
        else:
            ordered_node_ids = []
            node_ids = list(self.nodes.keys())
            while len(node_ids):
                for node_id in node_ids:
                    schedule = True
                    for link in self.links.values():
                        if link.to_node_id == node_id and link.from_node_id not in ordered_node_ids:
                            schedule = False
                            break
                    if schedule:
                        ordered_node_ids.append(node_id)
                        node_ids.remove(node_id)
            if traversal_order == False:
                ordered_node_ids.reverse()
            return ordered_node_ids

    def get_node_ids_to(self, node_id):
        pred_node_ids = {node_id}
        for link in self.links.values():
            if link.to_node_id == node_id:
                node_ids = self.get_node_ids_to(link.from_node_id)
                for pred_node_id in node_ids:
                    pred_node_ids.add(pred_node_id)
        return list(pred_node_ids)

    def get_node_ids_from(self, node_id):
        succ_node_ids = {node_id}
        for link in self.links.values():
            if link.from_node_id == node_id:
                node_ids = self.get_node_ids_from(link.to_node_id)
                for succ_node_id in node_ids:
                    succ_node_ids.add(succ_node_id)
        return list(succ_node_ids)

    def add_link(self, link, loading=False):
        link_id = link.get_link_id()
        self.links[link_id] = link
        if not loading:
            self.__save_dir()
        for callback in self.add_link_callbacks:
            callback(link)
        return link

    def get_link(self, link_id):
        return self.links.get(link_id,None)

    def get_link_ids(self):
        return list(self.links.keys())

    def set_metadata(self, metadata, loading=False):
        self.metadata = deepcopy(metadata)
        if not loading:
            self.__save_dir()

    def get_metadata(self):
        return deepcopy(self.metadata)

    def remove_node(self, node_id):
        if node_id in self.nodes:
            node = self.nodes[node_id]
            del self.nodes[node_id]
            for callback in self.remove_node_callbacks:
                callback(node)

        if self.savedir is not None:
            file_storage = os.path.join(self.savedir,"nodes",node_id)
            if os.path.exists(file_storage):
                try:
                    shutil.rmtree(file_storage)
                except:
                    self.logger.exception(f"Unable to remove directory {file_storage} when removing node")

        del self.node_datastores[node_id]
        self.__save_dir()

    def remove_link(self, link_id):
        if link_id in self.links:
            link = self.links[link_id]
            del self.links[link_id]
            for callback in self.remove_link_callbacks:
                callback(link)
        self.__save_dir()

    def clear(self):
        self.nodes = {}
        self.links = {}
        for callback in self.clear_network_callbacks:
            callback()
        self.__save_dir()

    def get_input_ports(self, node_id):
        node = self.nodes.get(node_id,None)
        if node:
            node_type = self.schema.get_node_type(node.get_node_type())
            input_ports = []
            for (input_port_name, _) in node_type.get_input_ports():
                input_ports.append(input_port_name)
            return input_ports
        else:
            return []

    def get_output_ports(self, node_id):
        node = self.nodes.get(node_id,None)
        if node:
            node_type = self.schema.get_node_type(node.get_node_type())
            output_ports = []
            for (output_port_name, _) in node_type.get_output_ports():
                output_ports.append(output_port_name)
            return output_ports
        else:
            return []

    def get_inputs_to(self, node_id, input_port_name=None):
        inputs = []
        for link in self.links.values():
            if link.to_node_id == node_id and (input_port_name is None or link.to_port == input_port_name):
                inputs.append((link.from_node_id, link.from_port))
        return inputs

    def get_outputs_from(self, node_id, output_port_name=None):
        outputs = []
        for link in self.links.values():
            if link.from_node_id == node_id and (output_port_name is None or link.from_port == output_port_name):
                outputs.append((link.to_node_id, link.to_port))
        return outputs

    def get_terminal_nodes(self):
        node_ids = set(self.nodes.keys())
        for link in self.links.values():
            node_ids.remove(link.from_node_id)
        return node_ids

    def load(self, from_dict, node_renamings, link_renamings, loading=True):

        added_node_ids = []
        added_link_ids = []

        nodes = from_dict.get("nodes", {})
        for (node_id, node_content) in nodes.items():
            # check for collision with existing node ids, rename if necessary

            renamed = node_id in node_renamings
            node_id = node_renamings.get(node_id,node_id)

            added_node_ids.append(node_id)
            node = Node.load(node_id, node_content["node_type"], node_content)
            if renamed:
                node.x += 100
                node.y += 100
            self.add_node(node, loading=loading)

        links = from_dict.get("links", {})
        for (link_id, link_content) in links.items():
            # check for collision with existing links ids, rename if necessary
            link_id = link_renamings.get(link_id,link_id)
            added_link_ids.append(link_id)
            link = Link.load(link_id, link_content, node_renamings)
            self.add_link(link, loading=loading)

        # do not overwrite existing metadata...
        metadata = self.get_metadata()
        new_metadata = from_dict.get("metadata", {})
        for key in new_metadata:
            if key not in metadata:
                metadata[key] = new_metadata[key]
        self.set_metadata(metadata, loading=loading)
        return (added_node_ids, added_link_ids)

    def get_renamings(self, from_dict):

        nodes = from_dict.get("nodes", {})
        node_renamings = {}
        for node_id in nodes:
            if node_id in self.nodes:
                node_renamings[node_id] = "n" + str(uuid.uuid4())

        link_renamings = {}
        links = from_dict.get("links", {})
        for link_id in links:
            if link_id in self.links:
                link_renamings[link_id] = "l" + str(uuid.uuid4())

        return node_renamings, link_renamings


    def load_zip(self, f, merging=False):

        with zipfile.ZipFile(f) as zf:

            topology = json.loads(zf.read("topology.json").decode("utf-8"))
            node_renamings, link_renamings = self.get_renamings(topology)

            zipinfos = zf.infolist()

            extract_zipinfos = [zipinfo for zipinfo in zipinfos if zipinfo.filename.startswith("node") or zipinfo.filename.startswith("configuration")]

            for zipinfo in extract_zipinfos:
                if merging and zipinfo.filename.startswith("configuration"):
                    continue # if merging, do not overwrite existing package properties and data
                b = zf.read(zipinfo)
                # filename format is one of:
                #     node/<node_id>/properties.json
                #     node/<node_id>/data/<data_key>
                #     configuration/<package_id>/properties.json
                #     configuration/<package_id>/data/<data_key>

                components = zipinfo.filename.split("/")
                if components[0] == "node":
                    node_id = components[1]
                    if node_id in node_renamings:
                        node_id = node_renamings[node_id]
                    dsu = self.get_node_datastore(node_id)
                    if components[2] == "properties.json":
                        properties = json.loads(b.decode("utf-8"))
                        dsu.set_properties(properties)
                    elif components[2] == "data":
                        data_key = components[3]
                        dsu.set_data(data_key, b)
                elif components[0] == "configuration":
                    package_id = components[1]
                    dsu = self.get_configuration_datastore(package_id)
                    if components[2] == "properties.json":
                        properties = json.loads(b.decode("utf-8"))
                        dsu.set_properties(properties)
                    elif components[2] == "data":
                        data_key = components[3]
                        dsu.set_data(data_key, b)

            (added_node_ids, added_link_ids) = self.load(topology, node_renamings, link_renamings, loading=True)
            self.__save_dir()
            return (added_node_ids, added_link_ids, node_renamings)

    def load_dir(self):
        json_path = os.path.join(self.savedir, "topology.json")
        loaded_node_ids = []
        loaded_link_ids = []

        if os.path.exists(json_path):
            with open(json_path) as f:
                saved_topology = json.loads(f.read())
                node_renamings, link_renamings = self.get_renamings(saved_topology)
                (loaded_node_ids, loaded_link_ids) = self.load(saved_topology,node_renamings,link_renamings,
                                                                               loading=True)
        return (loaded_node_ids, loaded_link_ids, node_renamings)

    def save(self):
        saved = {"nodes": {}, "links": {}}

        for (node_id, node) in self.nodes.items():
            saved["nodes"][node_id] = node.save()

        for (link_id, link) in self.links.items():
            saved["links"][link_id] = link.save()

        saved["metadata"] = deepcopy(self.metadata)
        return saved

    def save_zip(self, to_file=None, include_data=True):
        saved = self.save()
        f = to_file if to_file else io.BytesIO()
        zf = zipfile.ZipFile(f, "w")
        zf.writestr("topology.json", json.dumps(saved,indent=4))
        for subdir in ["node","configuration"]:
            content_folder = os.path.join(self.savedir,subdir)
            if os.path.isdir(content_folder):
                for target_id in os.listdir(content_folder):
                    properties_path = os.path.join(self.savedir,subdir,target_id,"properties.json")
                    if os.path.exists(properties_path):
                        entry = os.path.join(subdir,target_id,"properties.json")
                        zf.write(properties_path, entry)
                    if include_data:
                        data_folder = os.path.join(self.savedir,subdir,target_id,"data")
                        if os.path.exists(data_folder):
                            for data_file in os.listdir(data_folder):
                                entry = os.path.join(subdir,target_id,"data",data_file)
                                zf.write(os.path.join(data_folder,data_file),entry)
        zf.close()
        if to_file is None:
            return f.getvalue()

    def __save_dir(self):
        if self.savedir:
            saved = self.save()
            path = os.path.join(self.savedir,"topology.json")
            with open(path,"w") as f:
                f.write(json.dumps(saved,indent=4))

