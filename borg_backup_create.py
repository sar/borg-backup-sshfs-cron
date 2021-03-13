#!/usr/bin/env python3
# Doc: Create new borg backup to existing repository
# Usage:
#  PYTHONPATH=.venv/bin ./borg-create-backup -p <mounted_dir> -r <repo_subdir> -n <backup_name> -d <local_dir>

import argparse
import os
import subprocess
import math
import time

"""Timestamp"""
timestamp = str(math.trunc(time.time()))

"""Local path default variable"""
localpath = os.getcwd()

"""Args required for runtime
Pass properties:
"""
parser = argparse.ArgumentParser(
    description='Create new borg backup to existing repository',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '--path', '-p',
    metavar='PATH',
    type=str,
    required=True,
    help='Local dir of remote mounted path with sshfs where borg repositories are located.'
)

parser.add_argument(
    '--repo', '-r',
    metavar='PATH',
    type=str,
    required=True,
    help='Borg backup repository subdir name located inside mounted path.'
)

parser.add_argument(
    '--name', '-n',
    metavar='NAME',
    type=str,
    default=timestamp,
    required=False,
    help='Optional: backup name, defaults to timestamp.'
)

parser.add_argument(
    '--local', '-d',
    metavar='PATH',
    type=str,
    default=localpath,
    required=False,
    help='Optional: path to local directory to backup, defaults to cwd.'
)


def main():
    """Borg backup command main entrypoint
    """
    args = parser.parse_args()

    cmd = f"borg create --stats {args.path}/{args.repo}::{args.name} {args.local}"
    subprocess.run(cmd)


"""Init"""
if __name__ == '__main__':
    main()
