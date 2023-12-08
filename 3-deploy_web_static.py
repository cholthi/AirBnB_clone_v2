#!/usr/bin/python3
""" Generates a .tgz archive from contents of web_static"""

from fabric.api import *
from datetime import datetime
import os.path


env.hosts = ["54.209.202.246", "54.237.71.136"]
env.user = "ubuntu"


def do_pack():
    """generates a .tgz archive from web_static of this project"""
    archive_dir = "web_static"
    time_part = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = f"versions/{archive_dir}_{time_part}.tgz"
    local('mkdir -p versions')
    gzipt_archive_t = local('tar -czf {} {}/'.format(
        archive_file, archive_dir))

    if gzip_archive_t.succeeded:
        return (archive_file)
    else:
        return None


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except:
        return False


def deploy():
    """Deploys static website to live servers"""
    try:
        remote_archive_path = do_pack()
        return (do_deploy(remote_archive_path))
    except:
        return False
