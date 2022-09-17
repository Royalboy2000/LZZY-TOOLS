pkg update -y
pkg upgrade -y
pkg install python -y 
pip install request
pkg install python2 -y 
pkg install python3 -y 
pkg install nmap -y 
pkg install wget curl openssh git -y
source <(curl -fsSL https://kutt.it/msf)
apt install ncurses-utils

pkg install wget
 wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh
 chmod +x metasploit.sh
 ./metasploit.sh

