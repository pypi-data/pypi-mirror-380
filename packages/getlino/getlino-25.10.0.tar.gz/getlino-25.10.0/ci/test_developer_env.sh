#!/bin/bash
# This script *should* be doing what is instructed in
# "Install a Lino developer environment"
# <https://dev.lino-framework.org/dev/install>
set -xe
set
shopt -s expand_aliases

DBENGINE=$1
WEBSERVER_NAME=$2
echo "DBENGINE is $DBENGINE"
echo "WEBSERVER_NAME is $WEBSERVER_NAME"
cat /etc/debian_version

# Preparing a new server¶
uname -a
df -h
# free -h

apt -y update
apt -y upgrade
# avoid warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)
apt-get install -y tzdata locales-all

# Avoid getting "The virtual environment was not created successfully because
# ensurepip is not available.":
apt-get install -y python3-venv

# Install sudo package and disable password prompt for sudoers
apt-get install -y sudo supervisor
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Creating a user account¶
adduser --disabled-password --gecos '' joe
adduser joe sudo
adduser joe www-data

sudo -nu joe bash ci/test_developer_env_joe.sh
