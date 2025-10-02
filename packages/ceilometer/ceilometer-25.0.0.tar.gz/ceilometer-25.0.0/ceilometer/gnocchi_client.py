#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from gnocchiclient import client
from gnocchiclient import exceptions as gnocchi_exc
import keystoneauth1.session
from oslo_log import log
from oslo_utils import versionutils

from ceilometer import keystone_client

LOG = log.getLogger(__name__)


def get_gnocchiclient(conf, request_timeout=None):
    group = conf.gnocchi.auth_section
    session = keystone_client.get_session(conf, group=group,
                                          timeout=request_timeout)
    adapter = keystoneauth1.session.TCPKeepAliveAdapter(
        pool_maxsize=conf.max_parallel_requests)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    interface = conf[group].interface
    region_name = conf[group].region_name
    gnocchi_url = session.get_endpoint(service_type='metric',
                                       service_name='gnocchi',
                                       interface=interface,
                                       region_name=region_name)
    return client.Client(
        '1', session, adapter_options={'connect_retries': 3,
                                       'interface': interface,
                                       'region_name': region_name,
                                       'endpoint_override': gnocchi_url})


# NOTE(sileht): This is the initial resource types created in Gnocchi
# This list must never change to keep in sync with what Gnocchi early
# database contents was containing
resources_initial = {
    "image": {
        "name": {"type": "string", "min_length": 0, "max_length": 255,
                 "required": True},
        "container_format": {"type": "string", "min_length": 0,
                             "max_length": 255, "required": True},
        "disk_format": {"type": "string", "min_length": 0, "max_length": 255,
                        "required": True},
    },
    "instance": {
        "flavor_id": {"type": "string", "min_length": 0, "max_length": 255,
                      "required": True},
        "image_ref": {"type": "string", "min_length": 0, "max_length": 255,
                      "required": False},
        "host": {"type": "string", "min_length": 0, "max_length": 255,
                 "required": True},
        "display_name": {"type": "string", "min_length": 0, "max_length": 255,
                         "required": True},
        "server_group": {"type": "string", "min_length": 0, "max_length": 255,
                         "required": False},
    },
    "instance_disk": {
        "name": {"type": "string", "min_length": 0, "max_length": 255,
                 "required": True},
        "instance_id": {"type": "uuid", "required": True},
    },
    "instance_network_interface": {
        "name": {"type": "string", "min_length": 0, "max_length": 255,
                 "required": True},
        "instance_id": {"type": "uuid", "required": True},
    },
    "volume": {
        "display_name": {"type": "string", "min_length": 0, "max_length": 255,
                         "required": False},
    },
    "swift_account": {},
    "ceph_account": {},
    "network": {},
    "identity": {},
    "ipmi": {},
    "stack": {},
    "host": {
        "host_name": {"type": "string", "min_length": 0, "max_length": 255,
                      "required": True},
    },
    "host_network_interface": {
        "host_name": {"type": "string", "min_length": 0, "max_length": 255,
                      "required": True},
        "device_name": {"type": "string", "min_length": 0, "max_length": 255,
                        "required": False},
    },
    "host_disk": {
        "host_name": {"type": "string", "min_length": 0, "max_length": 255,
                      "required": True},
        "device_name": {"type": "string", "min_length": 0, "max_length": 255,
                        "required": False},
    },
}

# NOTE(sileht): Order matter this have to be considered like alembic migration
# code, because it updates the resources schema of Gnocchi
resources_update_operations = [
    {"desc": "add volume_type to volume",
     "type": "update_attribute_type",
     "resource_type": "volume",
     "data": [{
         "op": "add",
         "path": "/attributes/volume_type",
         "value": {"type": "string", "min_length": 0, "max_length": 255,
                   "required": False}
     }]},
    {"desc": "add flavor_name to instance",
     "type": "update_attribute_type",
     "resource_type": "instance",
     "data": [{
         "op": "add",
         "path": "/attributes/flavor_name",
         "value": {"type": "string", "min_length": 0, "max_length": 255,
                   "required": True, "options": {'fill': ''}}
     }]},
    {"desc": "add nova_compute resource type",
     "type": "create_resource_type",
     "resource_type": "nova_compute",
     "data": [{
         "attributes": {"host_name": {"type": "string", "min_length": 0,
                        "max_length": 255, "required": True}}
     }]},
    {"desc": "add manila share type",
     "type": "create_resource_type",
     "resource_type": "manila_share",
     "data": [{
         "attributes": {"name": {"type": "string", "min_length": 0,
                                 "max_length": 255, "required": False},
                        "host": {"type": "string", "min_length": 0,
                                 "max_length": 255, "required": True},
                        "protocol": {"type": "string", "min_length": 0,
                                     "max_length": 255, "required": False},
                        "availability_zone": {"type": "string",
                                              "min_length": 0,
                                              "max_length": 255,
                                              "required": False},
                        "status": {"type": "string", "min_length": 0,
                                   "max_length": 255,
                                   "required": True}}
     }]},
    {"desc": "add volume provider resource type",
     "type": "create_resource_type",
     "resource_type": "volume_provider",
     "data": [{
         "attributes": {}
     }]},
    {"desc": "add volume provider pool resource type",
     "type": "create_resource_type",
     "resource_type": "volume_provider_pool",
     "data": [{
         "attributes": {"provider": {"type": "string", "min_length": 0,
                                     "max_length": 255, "required": True}}
     }]},
    {"desc": "add ipmi sensor resource type",
     "type": "create_resource_type",
     "resource_type": "ipmi_sensor",
     "data": [{
         "attributes": {"node": {"type": "string", "min_length": 0,
                                 "max_length": 255, "required": True}}
     }]},
    {"desc": "add launched_at to instance",
     "type": "update_attribute_type",
     "resource_type": "instance",
     "data": [
         {"op": "add", "path": "/attributes/launched_at",
          "value": {"type": "datetime", "required": False}},
         {"op": "add", "path": "/attributes/created_at",
          "value": {"type": "datetime", "required": False}},
         {"op": "add", "path": "/attributes/deleted_at",
          "value": {"type": "datetime", "required": False}},
     ]},
    {"desc": "add instance_id/image_id to volume",
     "type": "update_attribute_type",
     "resource_type": "volume",
     "data": [
         {"op": "add", "path": "/attributes/image_id",
          "value": {"type": "uuid", "required": False}},
         {"op": "add", "path": "/attributes/instance_id",
          "value": {"type": "uuid", "required": False}},
     ]},
    {"desc": "add availability_zone to instance",
     "type": "update_attribute_type",
     "resource_type": "instance",
     "data": [{
         "op": "add",
         "path": "/attributes/availability_zone",
         "value": {"type": "string", "min_length": 0, "max_length": 255,
                   "required": False}
     }]},
    {"desc": "add volume_type_id to volume",
     "type": "update_attribute_type",
     "resource_type": "volume",
     "data": [{
         "op": "add",
         "path": "/attributes/volume_type_id",
         "value": {"type": "string", "min_length": 0, "max_length": 255,
                   "required": False}
     }]},
    {"desc": "add storage_policy to swift_account",
     "type": "update_attribute_type",
     "resource_type": "swift_account",
     "data": [{
         "op": "add",
         "path": "/attributes/storage_policy",
         "value": {"type": "string", "min_length": 0, "max_length": 255,
                   "required": False}  # Only containers have a storage policy
     }]},
    {"desc": "make host optional for instance",
     "type": "update_attribute_type",
     "resource_type": "instance",
     "data": [{
         "op": "add",  # Usually update, the attribute likely already exists
         "path": "/attributes/host",
         "value": {"type": "string", "min_length": 0, "max_length": 255,
                   "required": False}  # Allow the hypervisor to be withheld
     }]},
]


REQUIRED_VERSION = "4.2.0"


def upgrade_resource_types(conf):
    gnocchi = get_gnocchiclient(conf)

    gnocchi_version = gnocchi.build.get()
    if not versionutils.is_compatible(REQUIRED_VERSION, gnocchi_version):
        raise Exception("required gnocchi version is %s, got %s" %
                        (REQUIRED_VERSION, gnocchi_version))

    for name, attributes in resources_initial.items():
        try:
            gnocchi.resource_type.get(name=name)
        except (gnocchi_exc.ResourceTypeNotFound, gnocchi_exc.NotFound):
            rt = {'name': name, 'attributes': attributes}
            gnocchi.resource_type.create(resource_type=rt)

    for ops in resources_update_operations:
        if ops['type'] == 'update_attribute_type':
            rt = gnocchi.resource_type.get(name=ops['resource_type'])
            first_op = ops['data'][0]
            attrib = first_op['path'].replace('/attributes/', '')
            # Options are only used when adding/updating attributes.
            # Make a shallow copy of the new value type, and remove options
            # from the copy to make sure it isn't included in checks.
            value = first_op['value'].copy()
            value.pop('options', None)
            if (first_op['op'] == 'add'
                    and attrib in rt['attributes']
                    and value == rt['attributes'][attrib]):
                continue
            if first_op['op'] == 'remove' and attrib not in rt['attributes']:
                continue
            gnocchi.resource_type.update(ops['resource_type'], ops['data'])
        elif ops['type'] == 'create_resource_type':
            try:
                gnocchi.resource_type.get(name=ops['resource_type'])
            except (gnocchi_exc.ResourceTypeNotFound, gnocchi_exc.NotFound):
                rt = {'name': ops['resource_type'],
                      'attributes': ops['data'][0]['attributes']}
                gnocchi.resource_type.create(resource_type=rt)
