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
        message('warning', f'{FILES_PATH} already exists')
    else:
        message('action', f"Downloading AEL files...")
        execute(f"git clone {FILES_URL} {FILES_PATH}")

if __name__ == '__main__':

    get_files()

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
