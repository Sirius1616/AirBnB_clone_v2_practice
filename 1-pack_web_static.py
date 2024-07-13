#!/usr/bin/python3
from fabric.api import local
from time import strftime


def do_pack():
    """A script that creates an zip archive for packing up files to be deployed"""
    
    time_format = strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(file_name))
        
        return "versions/web_static_{}.tgz".format(time_format)

    except Exception as e:
        return None
