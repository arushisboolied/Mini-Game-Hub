#!/bin/bash

echo "__  __ ___ _   _ ___    ____    _    __  __ _____   _   _ _   _ ____  
|  \/  |_ _| \ | |_ _|  / ___|  / \  |  \/  | ____| | | | | | | | __ ) 
| |\/| || ||  \| || |  | |  _  / _ \ | |\/| |  _|   | |_| | | | |  _ \ 
| |  | || || |\  || |  | |_| |/ ___ \| |  | | |___  |  _  | |_| | |_) |
|_|  |_|___|_| \_|___|  \____/_/   \_\_|  |_|_____| |_| |_|\___/|____/ 
"

FILE="./hub/users.tsv"
touch "$FILE"

hash_password() {
    echo -n "$1" | sha256sum | awk '{print $1}'
}

is_alphanumeric() {
    [[ "$1" =~ ^[a-zA-Z0-9]+$ ]]
}

user_exists() {
    grep -q "^$1	" "$FILE"
}

get_stored_hash() {
    grep "^$1	" "$FILE" | cut -f2
}

register_user() {
    local username=$1
    local password=$2
    local hash=$(hash_password "$password")
    echo -e "$username\t$hash" >> "$FILE"
}

update_password() {
    local username=$1
    local new_hash=$2
    awk -F'\t' -v user="$username" -v hash="$new_hash" 'BEGIN{OFS="\t"} $1==user {$2=hash} {print}' "$FILE" > temp && mv temp "$FILE"
}

delete_user() {
    local username=$1
    grep -v "^$username	" "$FILE" > temp && mv temp "$FILE"
}

secure_input() {
    echo -n "$1"
    read -s INPUT
    echo
}

authenticate_user() {
    while true; do
        read -p "Enter username: " username

        if ! is_alphanumeric "$username"; then
            echo "Username must be alphanumeric only."
            continue
        fi

        secure_input "Enter password: "
        password="$INPUT"

        if user_exists "$username"; then
            stored_hash=$(get_stored_hash "$username")
            input_hash=$(hash_password "$password")

            if [ "$stored_hash" == "$input_hash" ]; then
                echo "Login successful: $username"

                while true; do
                    echo "1) Continue"
                    echo "2) Change Password"
                    echo "3) Delete Account"
                    read -p "Choose option: " opt

                    case $opt in
                        1)
                            AUTH_USER="$username"
                            return
                            ;;
                        2)
                            secure_input "Enter current password: "
                            curr="$INPUT"
                            curr_hash=$(hash_password "$curr")

                            if [ "$curr_hash" != "$stored_hash" ]; then
                                echo "Incorrect current password."
                                continue
                            fi

                            secure_input "Enter new password: "
                            newpass="$INPUT"
                            secure_input "Confirm new password: "
                            confirm="$INPUT"

                            if [ "$newpass" != "$confirm" ]; then
                                echo "Passwords do not match."
                                continue
                            fi

                            new_hash=$(hash_password "$newpass")
                            update_password "$username" "$new_hash"
                            stored_hash="$new_hash"
                            echo "Password updated."
                            ;;
                        3)
                            secure_input "Enter password to confirm deletion: "
                            delpass="$INPUT"
                            del_hash=$(hash_password "$delpass")

                            if [ "$del_hash" != "$stored_hash" ]; then
                                echo "Incorrect password."
                                continue
                            fi

                            delete_user "$username"
                            echo "Account deleted. Please register again."
                            break
                            ;;
                        *)
                            echo "Invalid option."
                            ;;
                    esac
                done

            else
                echo "Incorrect password. Try again."
            fi

        else
            read -p "User not found. Register? (y/n): " choice
            if [ "$choice" == "y" ]; then
                register_user "$username" "$password"
                echo "Registered successfully: $username"
                AUTH_USER="$username"
                return
            fi
        fi
    done
}

echo "=== Player 1 ==="
authenticate_user
user1="$AUTH_USER"

while true; do
    echo "=== Player 2 ==="
    authenticate_user
    user2="$AUTH_USER"

    if [ "$user1" != "$user2" ]; then
        break
    else
        echo "Usernames must be distinct. Try again."
    fi
done

echo "Both users authenticated. Starting game..."
python3 ./hub/main.py "$user1" "$user2"