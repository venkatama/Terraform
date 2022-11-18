#!/usr/bin/python3

import os

def package_install(pack):
    return_data = {'Package': [] ,'Present': [] ,'command': [],}
    return_data['Package'].append(pack)
    pack = pack
    command = "sudo yum install "+ pack + " -y"
    print(command)
    return_data['command'].append(command)
    try:
         os.system(command)
         return_data['Present'].append("True")
    except:
         return_data['Present'].append("Failed to Install")

    return return_data

package_install("httpd")
