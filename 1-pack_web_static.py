#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
folder
"""

from fabric.api import local, env
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if the archive has been correctly generated,
        None otherwise
    """
    # Create versions folder if not exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate archive path
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{timestamp}.tgz'
    archive_path = os.path.join('versions', archive_name)

    # Command to create the archive
    command = f'tar -cvzf {archive_path} web_static'

    # Execute the command
    try:
        local(command)
        print(f'packing web_static to {archive_path}')
        return archive_path
    except Exception as e:
        print(f'Error packing web_static: {e}')
        return None

def pack():
    """
    Default task to pack the web_static folder
    """
    archive_path = do_pack()
    if archive_path:
        print(f'Packed: {archive_path}')
    else:
        print('Failed to pack web_static.')
