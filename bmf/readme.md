# BUPMF (Backup Manifest)

Example manifest format:
```
MKBMF: generate backup manifest and metadata
found 5 files
%%%% MKBMF-1.0
%%%% size,sha1,access,user,group,mtime,path
## Invoked from: /path/to/archive
## Argument: .
##
4096    ------------------DIR!------------------        drwxr-xr-x      1000    1000    2021-06-20 20:16:44.988620831 -0400     .
0       da39a3ee5e6b4b0d3255bfef95601890afd80709        -rw-r--r--      1000    1000    2021-06-20 20:16:44.988620831 -0400     ./empty
```

## Additional Features

- `scan` - create the list file
- `listdup` - find and show duplicates (files with the same sha1sum)
- `diff` - show changes
- `diffall` - show changes (all)
    - e.g. deleted directory implies deletion all child items, but this is omitted in `diff` subcommand
