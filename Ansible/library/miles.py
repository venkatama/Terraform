#!/usr/bin/python3
#
from ansible.module_utils.basic import *
def transfer_mode(miles):

    return_data = {'Mode': [] , 'distance': []}
    distance = miles
    if distance <= 3:
        mode = 'walking'
    elif distance > 3 and miles <=300:
        mode = 'Driving'
    elif distance > 300:
        mode = 'Flying'
    return_data['Mode'].append(mode)
    return return_data

def main():
    fields = {
            "Miles": {"required": True, "type": "int"},
    }
    module = AnsibleModule(argument_spec=fields)
    new_key = transfer_mode(module.params)
    module.exit_json(changed=False, msg_output=new_key)

if __name__ == '__main__':
    main()
