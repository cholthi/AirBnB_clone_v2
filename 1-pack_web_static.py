#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder
"""
from datetime import date
import time import strftime
from fabric.api import local


def do_pack():
    """Generates an archive."""
    filename = None
    try:
        tme = time.strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(tme))
        filename = "versions/web_static_{}.tgz web_static/".format(tme)
    except Exception:
        pass
    return filename


