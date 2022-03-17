#!/usr/bin/env bash


i=1
while [ "$i" -ge 0 ]; do
    echo -n .
    echo -e "{\n\t\"sequence\": $i \n\t\"timestamp\": \"`date +%s.%N`\"\n}" | openssl aes-256-cbc -nosalt -pbkdf2 -k supersecretpassword > /dev/udp/localhost/7111
    sleep 1
done&

while :
do
    nc -luvw 0 localhost 7111  | openssl aes-256-cbc -d -nosalt -pbkdf2 -k supersecretpassword
done
