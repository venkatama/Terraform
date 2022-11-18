#!/usr/bin/python3
#
from ansible.module_utils.basic import *
def create_log(ymldoc):

    return_data = {'status': [], 'content': []}
    filepath = ymldoc['path']
    content = ymldoc['content']
    logfile = open(filepath, "a")
    logfile.write(content)
    logfile.close()
    return_data['status'] = "File has been updated"
    return_data['content'] = content
    return return_data

def main():
    fields = {
        "content": {"required": True, "type": "str"},
        "path": {"required": True, "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)
    new_key = create_log(module.params)
    module.exit_json(changed=False, msg_output=new_key)

if __name__ == '__main__':
    main()
