#!/usr/bin/python3

import os
#from ansible.module_utils.basic import *
from subprocess import run, PIPE
pack = "httpd"
command = "sudo yum install " + pack
res = run(command, shell=True, stdout=PIPE, stderr=PIPE, check=True)
