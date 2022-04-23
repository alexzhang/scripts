#!/bin/sh

while :
do
    test -e /dev/sda
    if [ $? -eq 0 ]; then
        echo "!!! --- /dev/sda created --- !!!";
        break;
    else
        echo "waiting for /dev/sda...";
        sleep 1;
    fi
done

cryptsetup open --type=plain --cipher=aes-xts-plain64 --key-file=/root.key /dev/sda enc
losetup -o 1048576 -f /dev/mapper/enc
