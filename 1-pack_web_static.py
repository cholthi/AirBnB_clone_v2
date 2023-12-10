#!/usr/bin/python3
from fabric.api import local
from datetime import date
import time


def do_pack():
    """ A script to generate archive the contents of web_static folder"""

    tme = time.strftime("%Y%m%d%H%M%S")
    filename = None
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(tme))

        filename = "versions/web_static_{}.tgz".format(tme)

    except Exception:
        pass
    return filename
