#!/bin/bash

if (( $EUID != 0 ));
then
    echo "/* Please, run as root! */"
    exit
fi

echo "/* Installing Docker */"

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

echo "/* Installing Kubelet, please wait a fill seconds.... */"

curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl


echo "/* Installinig Minikube */"

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64;
mv minikube-linux-amd64 /usr/local/bin/minikube;
