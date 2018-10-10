#!/bin/bash

echo 'Setup init...'
apt update -y
apt upgrade -y
echo -e 'Setp 1 Done.\n'


echo 'Install software...'
BASIC='man gcc make sudo lsof ssh openssl tree vim'
EXT='dnsutils iputils-ping net-tools psmisc sysstat'
NETWORK='curl telnet traceroute wget'
LIBS='libbz2-dev libpcre3 libpcre3-dev libreadline-dev libsqlite3-dev libssl-dev zlib1g-dev'
SOFTWARE='git mysql-server zip p7zip apache2-utils'
apt install -y $BASIC $EXT $NETWORK $LIBS $SOFTWARE
apt autoremove
apt autoclean
echo -e 'Setp 2 Done.\n'


echo 'Install pyenv...'
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
echo -e 'Setp 3 Done.\n'


echo 'Init pyenv...'
echo '
# PyenvConfig
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
' >> $HOME/.bashrc
source $HOME/.bashrc
pyenv update
echo -e 'Setp 4 Done.\n'


echo 'Install Python 3.6.6'
pyenv install -v 3.6.6
pyenv global 3.6.6
echo -e 'Setp 5 Done.\n'


echo 'Install python packages...'
cd `dirname $0`
pip install -U pip
pip install -r ../requirements.txt
cd -
echo -e 'Setp 6 Done.\n'


echo 'Install Nginx...'
cd /tmp/
wget 'http://nginx.org/download/nginx-1.14.0.tar.gz'
tar -xzf nginx-1.14.0.tar.gz
cd nginx-1.14.0
./configure
make
make install
rm -rf nginx*
cd -
echo -e 'Setp 8 Done.\n'


echo 'Install Redis'
cd /tmp/
wget 'http://download.redis.io/releases/redis-4.0.11.tar.gz'
tar -xzf redis-4.0.11.tar.gz
cd redis-4.0.11
make && make install
cd -
echo -e 'Setp 9 Done.\n'
