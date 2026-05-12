git clone https://github.com/UluBeyCRS/Botnet-Tool.git

cd Botnet-Tool

#Kali linux

sudo apt update && sudo apt upgrade -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install git -y

python3 -m venv ufonet_env

source ufonet_env/bin/activate

pip3 install requests

sudo python3 botnet.py


#Termux

pkg update && pkg upgrade -y

pkg install python -y

pkg install git -y

pkg install openssl-tool -y

python -m venv ufonet_env

source ufonet_env/bin/activate

pip install requests

python botnet.py
