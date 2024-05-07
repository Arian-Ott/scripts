#!/bin/bash

# Check if GPG is installed
if ! command -v gpg &> /dev/null
then
    echo "GPG could not be found. Please install GPG to continue."
    exit 1
fi

# Setting default email


# Prompting the user for personal information
read -p "Please enter your full name: " full_name
read -p "Please enter your email [default: $DEFAULT_EMAIL]: " email
email=${email}


# Prompting for passphrase
read -s -p "Enter passphrase for the new key (hidden): " passphrase
echo
read -s -p "Confirm passphrase: " confirm_passphrase
echo

if [ "$passphrase" != "$confirm_passphrase" ]; then
    echo "Passphrases do not match. Please try again."
    exit 1
fi

# Confirm information
echo "You have entered the following information:"
echo "Name: $full_name"
echo "Email: $email"
read -p "Is this correct? (y/n) " correct

if [[ "$correct" =~ ^[Yy]$ ]]
then
    # Generate the key using a here-document to feed GPG the necessary options
    gpg --batch --pinentry-mode loopback --passphrase "$passphrase" --gen-key <<EOF
Key-Type: RSA
Key-Length: 4096
Key-Usage: sign
Name-Real: $full_name
Name-Email: $email
Expire-Date: 0
%commit
EOF
    echo "Key generation complete."
 KEY_ID=$(echo "$GPG_OUTPUT" | grep 'key [A-Z0-9]* marked as ultimately trusted' | grep -o '[A-Z0-9]\{8\}')

    # Export key ID to environment variable
    export INIT_GPG="$KEY_ID"
    echo "Key generation complete. Key ID $INIT_GPG has been set as an environment variable."
else
    echo "Key generation aborted by user."
    exit 0
fi
