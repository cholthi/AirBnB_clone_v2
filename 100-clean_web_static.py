#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['35.168.3.7', '100.25.170.135']


def do_clean(number=0):
    """ deletes out-of-date archives """
    archive_files = sorted(os.listdir("versions"))
    
    number = int(number) if int(number) != 0 else 1

    # clean archives from versions folder

    for i in range(number):
        archive_files.pop()
    # clean local hidden files
    with lcd("versions"):
        for arch in archive_files:
            local("rm ./{}".format(arch))
    # clean host
    with cd("/data/web_static/releases"):
        archive_files = run("ls -tr").split()
        archive_files = [ar for ar in archive_files if "web_static_" in ar]
        for i in range(number):
            archive_files.pop()
        for arch in archive_files:
            run("sudo rm -rf ./{}".format(arch))
