#bin/bash
apt update && apt upgrade -y > /dev/null
apt install python3.12, python3.12-venv, python3.12-pip -y > /dev/null
cd 
mkdir .setup 
cd .setup 
apt install curl > /dev/null
apt install git >/dev/null

git clone https://github.com/Arian-Ott/scripts/
python3.12 -m venv venv
source venv/bin/activate 
python3.12 -m pip install typer -y 
python3.12 scripts/aaa.py

cd ..
rm -rf .setup