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


class App2AppMessage:

    def __init__(self, from_workspace_id, from_app_name, from_service_id, data):
        self.from_workspace_id = from_workspace_id
        self.from_app_name = from_app_name
        self.from_service_id = from_service_id
        self.data = data

    def get_data(self):
        return self.data

    def get_from_workspace_id(self):
        return self.from_workspace_id

    def get_from_app_name(self):
        return self.from_app_name

    def get_from_service_id(self):
        return self.from_service_id

    def __repr__(self):
        return f"App2AppMessage({self.from_workspace_id},{self.from_app_name},{self.from_service_id},{str(self.data)})"