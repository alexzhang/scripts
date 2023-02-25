# BUPMF (Backup Manifest)

Example manifest format:
```
MKBMF: generate backup manifest and metadata
found 5 files
%%%% MKBMF-1.1
%%%% sha1,access,user,group,size,mtime,path
## Invoked from: /path/to/archive
## Path: .
##
------------------DIR!------------------        drwxr-xr-x      1000    1000    4096    2021-06-20 20:16:44.988620831 -0400     .
da39a3ee5e6b4b0d3255bfef95601890afd80709        -rw-r--r--      1000    1000    0       2021-06-20 20:16:44.988620831 -0400     ./empty
```
