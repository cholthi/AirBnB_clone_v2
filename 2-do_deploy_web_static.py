#!/usr/bin/python3
""" Generates a .tgz archive from contents of web_static"""

from fabric.api import local
from datetime import datetime
import os


env.hosts = ["54.209.202.246", "54.237.71.136"]
env.user = "ubuntu"

def do_pack():
    """generates a .tgz archive from web_static of this project"""
    archive_dir = "web_static"
    time_part = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = f"versions/{archive_dir}_{time_part}.tgz"
    try:
        local('mkdir -p versions')
        local('tar -czf {} {}/'.format(archive_file, archive_dir))
        return (archive_file)
    except:
        return None

def do_deploy(archive_path):
    """
        Deploy archive to nodes.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        release_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(release_version))
        sudo("tar -xzf {} -C {}/".format(archived_file,
                                             release_version))
        sudo("rm {}".format(archived_file))
        sudo("mv {}/web_static/* {}".format(release_version,
                                                release_version))
        sudo("rm -rf {}/web_static".format(release_version))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(release_version))

        print("New version deployed!")
        return True

    return False
