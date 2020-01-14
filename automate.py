import subprocess

## Preparando e instalando pacotes necessarios

subprocess.run(["apt-get", "update", "-y"])
subprocess.run(["apt-get", "upgrade", "-y"])
subprocess.run(["apt-get", "install", "nginx", "-y"])
subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
subprocess.run(["sh", "get-docker.sh"])

## Checando se os serviços estão com status active

def servicesToCheck():
    services = ['docker', 'nginx']

    for service in services:
        process =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
        (output, err) = process.communicate()
        output = output.decode('utf-8')
        

        if 'inactive' in output:
            print("Check os serviços", output) ## Aqui quero apresentar o nome do serviço que está out
        else:
            print("Serviços ativos....")

