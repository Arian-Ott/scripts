import typer

app = typer.Typer()
import os


def main():
    os.system("apt update && apt upgrade -y >> /dev/null 2>&1")
    lul = {}
    lul["default"] = typer.confirm("Install default? (Curl, net-tools, wget)")
    lul["portainer"] = typer.confirm("Install portainer?")
    lul["docker"] = typer.confirm("Install docker? (compose, engine...)")
    lul["ufw"] = typer.confirm("Install ufw?")
    lul["python"] = typer.confirm("Install python?")
    lul["git"] = typer.confirm("Install git?")
    lul["ssh"] = typer.confirm("Configure SSH keys")
    typer.secho("Config \n"+f"Default: {lul['default']}"
                f"\nPortainer: {lul['portainer']}"
                f"\nDocker: {lul['docker']}"
                f"\nUFW: {lul['ufw']}"
                f"\nPython: {lul['python']}"
                f"\nGit: {lul['git']}"
                f"\nSSH: {lul['ssh']}", color=typer.colors.CYAN)

    typer.confirm("Start installation", abort=True)
    os.system("clear")
    fsad = 0
    for i in lul.values():
        if i:
            fsad += 1
    x = typer.progressbar(length=fsad )

    os.system(f"apt update >> /dev/null 2>&1")
    x.update(1)
    os.system(f"apt upgrade -y >> /dev/null 2>&1")
    x.update(1)
    if lul["default"]:
        os.system(f"apt install curl -y && apt install net-tools -y  && apt install wget -y > /dev/null 2>&1")
        x.update(1)
    if lul["portainer"]:
        lul["docker"] = True

    if lul["docker"]:
        os.system(f"""sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc""")
        x.update(1)
        os.system(f"""echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$UBUNTU_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null""")
        os.system(f""" sudo apt-get update""")
        x.update(1)
        os.system(
            f"""sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y""")
        x.update(1)
    if lul["portainer"]:
        os.system(f"docker volume create portainer_data")
        x.update(1)
        os.system("""docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest""")
        x.update(1)
    if lul["ufw"]:
        os.system("apt install ufw")
        x.update(1)
        os.system("ufw allow 22")
        x.update(1)
        os.system("ufw allow 80")

        x.update(1)
        os.system("ufw allow 8000")
        x.update(1)
        os.system("ufw allow 9443")
        x.update(1)
        os.system("ufw allow 443")
        x.update(1)
        os.system("ufw enable")
        x.update(1)
    if lul["git"]:

        os.system(
        '''#!/bin/bash

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
''')





if __name__ == "__main__":
    main()