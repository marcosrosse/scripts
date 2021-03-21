#!/bin/bash

if (( $EUID != 0 ));
then
    echo  "Please, run as root!"
    exit
fi

## Check distros supported by the script in get docker 

MY_DISTRO=$(lsb_release -d|awk '{print $2}')
O_DISTROS=("Debian" , "Ubuntu" , "Fedora" , "CentOS")

if [ $DISTRO = O_DISTROS ]
then
    curl -sSFL https://get.docker.com | sh
else
    if !  command -v docker -v  &> /dev/null
      then
      pacman -Syyu docker;
      echo "Docker installed"
    else
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64;
    install minikube-linux-amd64 /usr/local/bin/minikube;
    echo "Minikibe has been installed"
    fi
fi