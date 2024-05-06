#bin/bash
apt update && apt upgrade -y > /dev/null
apt-get install python3.11 -y && apt-get install  python3.11-venv -y && apt-get install  python3-pip -y > /dev/null
cd
mkdir ~/.setup
cd ~/.setup
apt install curl > /dev/null
apt install git >/dev/null

git clone https://github.com/Arian-Ott/scripts/
python3 -m venv venv
source venv/bin/activate
python3 -m pip3 install typer -y
python3 ~/.setup/scripts/main.py

cd ..
#rm -rf .setup