#!/bin/bash 

touch "users.tsv"

#hashing passwords
hashing_passwords(){
    echo -n "$1" | sha256sum | awk '{print $1}'
}

#user existence
user_existence(){
    grep -q "^$1|" "users.tsv"
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
    echo "User '$username' has been registered successfully."
}

#user authentication
user_authentication(){
    local username
    local password
    while true; do
        echo -n " Enter Username: "
        read username

        if user_existence "$username"; then
            echo -n " Enter Password: "
            read -s password
            echo

            local hashed_input=$(hashing_passwords "$password")
            local stored_hash=$(fetch_hash "$username")

            if [ "$hashed_input" == "$stored_hash" ]; then
                echo "Authentication successful. Welcome, $username!"
                break
            else
                echo "Incorrect password. Please try again."
            fi
        else
            echo "Username '$username' does not exist."
            echo -n " Do you want to register? (y/n): "
            read response
            if [[ "$response" == "y" ]]; then
                echo -n " Enter Password for registration: "
                read -s password
                echo
                register_user "$username" "$password"
                echo "$username"
                return
            fi
        fi
    done
}

echo "---- Player 1 Authentication ----"
user1=$(user_authentication)

echo "---- Player 2 Authentication ----"
user2=$(user_authentication)

while true; do
    if [ "$user1" == "$user2" ]; then
        echo "Both players cannot have the same username. Please re-authenticate Player 2."
        user2=$(user_authentication)
    else
        break
    fi
done

echo "Both players authenticated successfully. Starting the game..."
python3 game.py "$user1" "$user2"