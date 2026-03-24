#!/bin/bash 

#hashing passwords
hashing_passwords(){
    echo -n "$1" | sha256sum | awk '{print $1}'
}

#user existence
user_existence(){
    cut -f1 "users.tsv" | grep -qx "$1"
}

#fetch hashed password
fetch_hash(){
    grep "^$1|" "users.tsv" | cut -d "|" -f2
}

#registering users
register_user(){
    local username="$1"
    local password="$2"
    local hashed_password=$(hashing_passwords "$password")
    echo "$username|$hashed_password" >> "users.tsv"
    echo "User '$username' has beenregistered successfully."
}