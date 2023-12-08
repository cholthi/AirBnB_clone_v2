#!/usr/bin/python3
""" Generates a .tgz archive from contents of web_static"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from web_static of this project"""
    archive_dir = "./web_static"
    time_part = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = f"versions/{archive_dir}_{time_part}.tgz"
    try:
        local('mkdir -p versions')
        local('tar -czf {} {}/'.format(archive_file, archive_dir))
        return (archive_file)
    except:
        return None
