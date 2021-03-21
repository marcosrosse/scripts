#!/bin/bash

if (( $EUID != 0 ));
then
    echo  "Please, run as root!"
    exit
fi

if !  command -v docker -v  &> /dev/null
then
   DISTRO=$( cat /etc/*-release | tr [:upper:] [:lower:] | grep -Poi '(debian|ubuntu|red hat|centos)' | uniq )
  if [ -z $DISTRO ]
  then
     pacman -Syyu docker;
  else
     curl -sSFL https://get.docker.com | sh

fi  
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64;
    install minikube-linux-amd64 /usr/local/bin/minikube;
    echo "Minikibe has been installed"