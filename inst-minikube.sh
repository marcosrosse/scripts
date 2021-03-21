#!/bin/bash

if (( $EUID != 0 ));
then
    echo  "Please, run as root!"
    exit
fi

if !  command -v docker -v  &> /dev/null
then
   DISTRO=$( cat /etc/*-release | tr [:upper:] [:lower:] | grep -Poi '(debian|ubuntu)' | uniq )
  if [ -z $DISTRO ]
  then
     yum update -y; 
     yum install -y docker;
     service start docker;
     service enable docker
  else
     curl -sSL https://get.docker.com | sh

fi
fi  
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64;
    install minikube-linux-amd64 /usr/local/bin/minikube;
    echo "Minikibe has been installed"