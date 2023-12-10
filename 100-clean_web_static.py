#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['35.168.3.7', '100.25.170.135']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """Delete out-of-date archives.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    
    # delete local archives
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    # delete host archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
