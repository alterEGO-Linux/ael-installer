## ----------------------------------------------------------------------- INFO
## [setup.py]
## author        : fantomH @alterEGO Linux
## created       : 2023-11-19 20:02:55 UTC
## updated       : 2023-11-19 20:02:55 UTC
## description   : ael-installer setup.py

from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

## Custom command to download data during installation
class CustomInstallCommand(install):
    def run(self):
        print('hello')
        ael_directory_path = '/usr/share/ael'
        os.makedirs(ael_directory_path, exist_ok=True)
        # Add your logic to download the data from the Git repository
        subprocess.check_call(['git', 'clone', 'https://github.com/alterEGO-Linux/ael-files.git', '/usr/share/ael/files'])
        # Continue with the default installation process
        install.run(self)

setup(
    name='ael-installer',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'toml',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    entry_points={
        'console_scripts': [
            'ael-installer = AELinstaller.sayhi:main',
        ],
    },
)

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
