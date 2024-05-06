#bin/bash
apt update && apt upgrade -y > /dev/null
apt install python3.12, python3.12-venv, python3.12-pip -y > /dev/null
cd 
mkdir .setup 
cd .setup 
python3.12 -m venv venv
source venv/bin/activate 
python3.12 -m pip install typer -y 
python3.12 main.py 
cd ..
apt install curl > /dev/null
rm -rf .setup