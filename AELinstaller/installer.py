## ----------------------------------------------------------------------- INFO
## [AELinstaller/installer.py]
## author        : fantomH @alerEGO Linux
## created       : 2023-11-20 00:23:25 UTC
## updated       : 2023-11-20 00:23:25 UTC
## description   : Installer and Updater.

import argparse
from collections import namedtuple
import os
import shlex
import shutil
import subprocess
import time
import tomllib

## Checking privileges.
if os.getenv('USER') == 'root':
    _user = 'root_user'
else:
    _user = 'normal_user'

## -------------------- [ UTILS ] 

## ---------- (* messages *) 
def message(msg_type, msg, wait=0):

    foreground_blue = '\033[34m'
    foreground_green = '\033[32m'
    foreground_red = '\033[31m'
    format_bold = '\033[1m'
    format_reset = '\033[00m'

    if msg_type == "action":
        print(f"{foreground_green}[*]{format_reset} {format_bold}{msg}{format_reset}")
    elif msg_type == "result":
        print(f"{foreground_blue}[-]{format_reset} {format_bold}{msg}{format_reset}")
    elif msg_type in ["warning", "error"]:
        print(f"{foreground_red}[!]{format_reset} {format_bold}{msg}{format_reset}")
    else:
        print(f"    {format_bold}{msg}{format_reset}")

    time.sleep(wait)

## ---------- (* execute *)
def execute(cmd, cwd=None, shell=False, text=True, input=None):

    if shell == True:
        cmd_list = cmd
    else:
        cmd_list = shlex.split(cmd)
    if input:
        input = input.encode()
        
    cmd_run = subprocess.run(cmd_list, cwd=cwd, shell=shell, input=input)

    CommandResults = namedtuple('CommandResults', ['returncode'])
    return CommandResults(cmd_run.returncode)

## -------------------- [ GIT ]

FILES_URL = 'https://github.com/alterEGO-Linux/ael-files.git'
FILES_PATH = '/usr/share/ael/cache/files'

def get_files():
    if os.path.isdir(FILES_PATH):
        message('action', f'Found {FILES_PATH}')
        message('results', f'Updating AEL files...')
        execute(f"git pull", cwd=FILES_PATH)
    else:
        message('action', f"Downloading AEL files...")
        execute(f"git clone {FILES_URL} {FILES_PATH}")

## -------------------- [ FILES ] 

def copy_files():
    FILES_CONFIG = os.path.join(FILES_PATH, 'usr', 'share', 'ael', 'files.toml')

    with open(FILES_CONFIG, 'rb') as _input:
        data = tomllib.load(_input)

        ## Convert dict of dict to namedtuple
        AELFiles = namedtuple('AELFiles', ['filename', 'src', 'dst', 'description', 'mode', 'is_symlink'])
        files_list = [AELFiles(**values) for values in data['file']['general'].values()]

        for f in files_list:
            print(f.filename)

if __name__ == '__main__':

    get_files()
    copy_files()

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
