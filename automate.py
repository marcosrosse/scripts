import subprocess
import os
import shutil
import sys

## Preparando e instalando pacotes necessarios

def preparing():
    subprocess.run(["apt-get", "update", "-y"])
    subprocess.run(["apt-get", "upgrade", "-y"])
    subprocess.run(["apt-get", "install", "nginx", "-y"])
    subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
    subprocess.run(["sh", "get-docker.sh"])
    os.remove("get-docker.sh")

preparing()

## Checando se os serviços estão com status active

def servicesToCheck():

    services = ['docker', 'nginx']
    for service in services:
        process =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
        (output, err) = process.communicate()
        output = output.decode('utf-8')
       
    if 'inactive' in output:
        print("Os seguintes serviços estão desativos:", service, "Será iniciado logo em seguida!")
        subprocess.Popen(["systemctl", "start", service])

servicesToCheck()

## Criando e exportando arquivos de virtualhosts do nginx

def touchVirtualHosts():

    pathNgnix = '/etc/nginx/conf.d/'
    fileName = ['app1.conf', 'app2.conf', 'app3.conf']
    os.path.join(pathNgnix, 'default.conf')
    confFilesNginx =(
    "server{\nlisten 80;\nserver_name app1.dexter.com.br; location /{\nproxy_pass http://35.193.203.135:8080/;\n}\n}",
    "server{\nlisten 80;\nserver_name app2.dexter.com.br; location /{\nproxy_pass http://35.193.203.135:8081/;\n}\n}",
    "server{\nlisten 80;\nserver_name app3.dexter.com.br; location /{\nproxy_pass http://35.193.203.135:8082/;\n}\n}"
    )

    for touching, config in zip (fileName, confFilesNginx):
        with open(pathNgnix + touching, 'w+') as file:
            file.writelines(config)

touchVirtualHosts()

## Criando estrutura de pastas

def structureDocker():

    content = ['app1', 'app2', 'app3']
    createStructure = ['/var/www/html/app1/public_html/', '/var/www/html/app2/public_html/', '/var/www/html/app3/public_html/']
    ports = ['8080', '8081', '8082']

    for createStruc, Content in zip (createStructure, content):
        pathToRemove = os.path.join("/var/www/html/", Content)

        if os.path.isdir(pathToRemove):
            shutil.rmtree(pathToRemove)
        os.makedirs(createStruc)
        
        with open(createStruc + "index.html", 'w+') as file:
            file.writelines(Content)
    
    for importFiles, ports, dockerNames in zip (createStructure, ports, content):
        executeDocker = ("docker run -dit --name {} -p {}:80 -v {}:/usr/local/apache2/htdocs/ httpd:2.4".format(dockerNames, ports, importFiles))
        subprocess.call([executeDocker], shell=True)

structureDocker()