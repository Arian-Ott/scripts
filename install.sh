#bin/bash
apt update && apt upgrade -y > /dev/null
apt-get install python3.11 -y >/dev/null && apt-get install  python3.11-venv -y > /dev/null && apt-get install  python3-pip -y > /dev/null
echo "installed python"
cd
mkdir ~/.setup
cd ~/.setup
apt install curl > /dev/null
echo "installed curl"
apt install git >/dev/null
echo "installed git"



git clone https://github.com/Arian-Ott/scripts/ > /dev/null
python3 -m venv venv
source venv/bin/activate
python3 -m pip install typer
echo "Install dependencies"
python scripts/main.py
deactivate
rm -rf venv
cd ..
rm -rf .setup
echo "DONE!"

exit 0
