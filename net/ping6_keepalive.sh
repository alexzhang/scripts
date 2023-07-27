#!/bin/sh

ping -6 -i 600 -s 0 -t 24 2600:: | while read line ; do echo "[`date --iso-8601=seconds`] ${line}"; done
