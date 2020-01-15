import subprocess
import os

## Preparando e instalando pacotes necessarios

# subprocess.run(["apt-get", "update", "-y"])
# subprocess.run(["apt-get", "upgrade", "-y"])
# subprocess.run(["apt-get", "install", "nginx", "-y"])
# subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
# subprocess.run(["sh", "get-docker.sh"])

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
        else:
            print("Serviço:", service,"ativo")

# servicesToCheck()

## Criando e exportando arquivos de virtualhosts do nginx

def touchVirtualHosts():
    pathNgnix = '/etc/nginx/conf.d/'
    fileName = ['app1.conf', 'app2.conf', 'app3.conf']
    os.path.join(pathNgnix, 'default.conf')
    # subprocess.run(["rm", "-f", pathNgnix,"default.conf"])
    confFilesNginx =(
    "server{\nlisten 80;\nserver_name app1.dexter.com.br; location /{\nproxy_pass http://10.215.47.45:8080/;\n}\n}",
    "server{\nlisten 80;\nserver_name app2.dexter.com.br; location /{\nproxy_pass http://10.215.47.45:8081/;\n}\n}",
    "server{\nlisten 80;\nserver_name app3.dexter.com.br; location /{\nproxy_pass http://10.215.47.45:8082/;\n}\n}"
    )

    for touching, config in zip (fileName, confFilesNginx):
        with open(pathNgnix + touching, 'w+') as file:
            file.writelines(config)

# touchVirtualHosts()

## Criando containers Docker

def DockerFile():
    # content = ['app1', 'app2', 'app3']
    createStructure = ['app1/public_html/', 'app2/public_html/', 'app3/public_html/']
    for createStruc in createStructure:
        os.makedirs(createStructure)
        # with open("/var/www/html/" + "index.html", 'w+') as file:
        #     file.writelines(Content)

DockerFile()

