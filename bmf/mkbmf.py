#!/usr/bin/env python3

import argparse
import os
import subprocess
import stat
import sys
from datetime import datetime, timezone

parser = argparse.ArgumentParser()
parser.add_argument('path', nargs='?', default='.', help='if omitted, uses the current path')
parser.add_argument('-np', '--no-perms', action='store_true', help='omit permissions when generating bmf')
parser.add_argument('-no', '--no-owner', action='store_true', help='omit owners when generating bmf')
parser.add_argument('-ng', '--no-group', action='store_true', help='omit groups when generating bmf')
parser.add_argument('-nt', '--no-times', action='store_true', help='omit times when generating bmf')
args = parser.parse_args()

print("\033[93mMKBMF: generate backup manifest and metadata\033[0m", file=sys.stderr)

### SEARCH FOR ALL FILES ###
try:
    result = subprocess.check_output(['find', args.path, '-print0'])
except:
    sys.exit(1)

files = result.decode('utf-8').split('\0')
files.pop()
print(f"\033[93mfound {len(files)} files\033[0m", file=sys.stderr)
s_files = sorted(files, key=lambda file: (os.path.dirname(file), os.path.basename(file)))
print(f"\033[93msorted {len(s_files)} files\033[0m", file=sys.stderr)

### HEADER OUTPUT ###
print("%%%% MKBMF-1.1")
print("%%%% sha1,", end='')
if not args.no_perms: print("access,", end='')
if not args.no_owner: print("user,", end='')
if not args.no_group: print("group,", end='')
print("size,", end='')
if not args.no_times: print("mtime,", end='')
print("path")
print(f"## Invoked from: {os.getcwd()}")
print(f"## Path: {args.path}")
print("##")

### PROCESS ALL FILES AND GET ATTRIBUTES ###
for file in s_files:
    stat_file = os.lstat(file)
    stat_buf = []
    if not args.no_perms:
        stat_buf.append(stat.filemode(stat_file.st_mode))
    if not args.no_owner:
        stat_buf.append(str(stat_file.st_uid))
    if not args.no_group:
        stat_buf.append(str(stat_file.st_gid))
    stat_buf.append(str(stat_file.st_size))
    temp_mtime, temp_mnano = divmod(stat_file.st_mtime_ns, 1_000_000_000)
    if not args.no_times:
        stat_buf.append('{}.{:09}Z'.format(
            datetime.fromtimestamp(temp_mtime, tz=timezone.utc).isoformat().removesuffix('+00:00'),
            temp_mnano
        ))
    name = str(file.encode('unicode-escape'))[2:-1]
    stat_str = '\t'.join(stat_buf)

    sha1sum = "NULL"
    if stat.S_ISDIR(stat_file.st_mode):
        sha1sum = "------------------DIR!------------------"
    elif stat.S_ISLNK(stat_file.st_mode):
        sha1sum = "------------------LINK------------------"
    else:
        sha1sum = subprocess.check_output(['sha1sum', file]).decode('utf-8').split(' ')[0]

    print(f"{sha1sum}\t{stat_str}\t{name}")
