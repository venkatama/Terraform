#!/usr/bin/python3

from ansible.module_utils.basic import *
import os

def package_install(pack):
    return_data = {'Package': [] ,'Present': [] ,'command': [],}
    pack = pack["pack"]
    return_data['Package'].append(pack)
    install_cmd = "sudo yum install "+ pack + " -y"
    return_data['command'].append(install_cmd)
    try:
         os.system(install_cmd)
         os.getcwd()
         return_data['Present'].append("True")
    except:
         return_data['Present'].append("Failed to Install")

    return return_data

def main():
    fields = {
            "pack": {"required": True, "type": "str"},
    }
    module = AnsibleModule(argument_spec=fields)
    new_key = package_install(module.params)
    module.exit_json(changed=False, msg_output=new_key)

if __name__ == '__main__':
    main()



