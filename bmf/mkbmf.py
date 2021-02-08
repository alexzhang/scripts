#!/usr/bin/env python3

import os
import subprocess
import sys

script = os.path.basename(sys.argv[0])

if len(sys.argv) != 2:
    print(f"\033[91m{script}: error: missing filename argument\033[0m", file=sys.stderr)
    sys.exit(1)

cwd = os.getcwd()
print("\033[93mMKBMF: generate backup manifest and metadata\033[0m", file=sys.stderr)

### SEARCH FOR ALL FILES ###
result = subprocess.check_output(['find', sys.argv[1], '-print0'])
files = result.decode('utf-8').split('\0')
blank_chk = files.pop()                                                 # remove last element from split since find command is NUL-terminated

if blank_chk == "":
    print(f"\033[93mfound {len(files)} files\033[0m", file=sys.stderr)
else:
    print(f"\033[91m{script}: error: unable to enumerate files\033[0m", file=sys.stderr)
    sys.exit(1)

### START OUTPUT ###

print("%%%% MKBMF-1.0")
print("%%%% size,sha1,access,user,group,mtime,path")
print(f"## Invoked from: {cwd}")
print(f"## Argument: {sys.argv[1]}")
print("##")

symlinks = 0

### PROCESS ALL FILES AND GET ATTRIBUTES ###
for file in files:
    result = subprocess.check_output(['stat', file, '-c', '%A,%u,%g,%s,%y'])
    access, user, group, size, mtime = result.decode('utf-8').strip().split(',')
    name = str(file.encode('unicode-escape'))[2:-1]

    sha1sum = "NULL"
    if access.startswith('d'):
        sha1sum = "------------------DIR!------------------"
    elif access.startswith('l'):
        sha1sum = "------------------LINK------------------"
    else:
        sha1sum = subprocess.check_output(['sha1sum', file]).decode('utf-8').split(' ')[0]

    print(f"{size}\t{sha1sum}\t{access}\t{user}\t{group}\t{mtime}\t{name}")
