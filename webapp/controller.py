

from device42_app.dal.model.device import DeviceVM
from device42_app.common.class_utils import create_object
from device42_app.dal.queries.insert import InsertOperations


def create_vm(attr_dict):
    vm_obj = create_object(DeviceVM, attr_dict)
    ins_obj = InsertOperations()
    ins_obj.insert_obj(vm_obj)

if __name__ == '__main__':

    a = {"device_type": "VM", "ip_address": "172.16.1.10", "hostname": "dev_vm", "service_level": "Internal", "customer": "Aws", "notes": "trying "}

    create_vm(a)