#!/bin/bash 

#hashing passwords
hashing_passwords(){
    echo -n "$1" | sha256sum | awk '{print $1}'
}

#user existence
user_existence(){
    cut -f1 "users.tsv" | grep -qx "$1"
}
