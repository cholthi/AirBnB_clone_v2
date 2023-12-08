#!/usr/bin/python3
from datetime import date
import time import strftime
from fabric.api import local


def do_pack():
    """ Generates an archive file using web_static"""
    try:
        tme = time.strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(tme))
        filename = "versions/web_static_{}.tgz web_static/".format(tme)
    except Exception:
        pass
    return filename
