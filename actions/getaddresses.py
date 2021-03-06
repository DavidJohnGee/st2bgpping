# encoding: utf-8

"""
Copyright 2017 Brocade Communications Systems, Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys

from st2actions.runners.pythonrunner import Action
from st2client.client import Client
from st2client.models import KeyValuePair

class GetNBGPPingAddresses(Action):
        
    def run(self):

        self.client = Client(base_url='http://localhost')
        queryresult = self.client.keys.query(prefix="NPING")
        iplist = []

        for key in queryresult:
            _name = key.name
            _ip = _name.split(':')[1]
            iplist.append(_ip)

        if iplist:
            return (True, iplist)
        return (False)
