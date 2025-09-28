import subprocess, sys
from asyncio.log import logger


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



if __name__ == '__main__':
    file_path = '../../ressources/presentation_ogiv.pptx'
    open_file(file_path)