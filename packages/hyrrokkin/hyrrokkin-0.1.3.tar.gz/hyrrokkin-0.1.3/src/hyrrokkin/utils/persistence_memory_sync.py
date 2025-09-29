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

import copy

from hyrrokkin_engine_drivers.persistence import Persistence

class PersistenceMemorySync:

    def __init__(self):
        self.properties = {}
        self.data = {}

    def get_properties(self):
        return copy.deepcopy(self.properties)

    def set_properties(self, properties):
        self.properties = copy.deepcopy(properties)

    def get_data_keys(self):
        return list(self.data.keys())

    def get_data(self, key):
        Persistence.check_valid_data_key(key)
        if key in self.data:
            return self.data[key]
        return None

    def set_data(self, key, data):
        Persistence.check_valid_data_key(key)
        Persistence.check_valid_data_value(data)
        if data is None:
            if key in self.data:
                del self.data[key]
        else:
            self.data[key] = data


