import subprocess, sys
from asyncio.log import logger
import importlib.resources as pkg_resources

def open_file(file_path):
    try:
        if sys.platform == 'linux':
            subprocess.run(['xdg-open', file_path])
        elif sys.platform == 'darwin':
            subprocess.run(['open', file_path])
        else:
            logger.error('Unsupported OS')
    except Exception as e:
        raise RuntimeError(f"Failed to open file: {e}")



def main():
    file = ''
    with pkg_resources.path('baudream.ressources', file) as file_path:
        open_file(file_path)