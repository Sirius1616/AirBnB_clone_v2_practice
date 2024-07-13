#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """A script that creates an zip archive for packing up files to be deployed"""
    
    try:
        local("mkdir -p versions")

        time_format = datetime.now().strftime("%Y%m%d%H%M%S")
        
        file_name = "versions/web_static_{}.tgz".format(time_format)
        local("tar -czvf {} web_static".format(file_name))
        
        return file_name

    except Exception as e:
        print(e)
        return None






