#!/usr/bin/python3
from datetime import date
import time import strftime
from fabric.api import local


def do_pack():
    """ Generates an archive file using web_static"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
