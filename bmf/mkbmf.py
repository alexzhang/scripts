#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


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

stat_format = "%A\t"
if not args.no_owner: stat_format += "%u\t"
if not args.no_group: stat_format += "%g\t"
stat_format += "%s\t"
if not args.no_times: stat_format += "%y\t"

### PROCESS ALL FILES AND GET ATTRIBUTES ###
for file in s_files:
    result = subprocess.check_output(['stat', file, '-c', stat_format])
    stat = result.decode('utf-8').strip()
    name = str(file.encode('unicode-escape'))[2:-1]

    sha1sum = "NULL"
    if stat.startswith('d'):
        sha1sum = "------------------DIR!------------------"
    elif stat.startswith('l'):
        sha1sum = "------------------LINK------------------"
    else:
        sha1sum = subprocess.check_output(['sha1sum', file]).decode('utf-8').split(' ')[0]

    if (args.no_perms):
        stat = stat.split('\t', 1)[1]
    print(f"{sha1sum}\t{stat}\t{name}")
