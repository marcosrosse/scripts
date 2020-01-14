import subprocess

## Preparando e instalando pacotes necessarios

subprocess.run(["apt-get", "update", "-y"])
subprocess.run(["apt-get", "upgrade", "-y"])
subprocess.run(["apt-get", "install", "nginx", "-y"])
subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
subprocess.run(["sh", "get-docker.sh"])

def servicesToCheck():
    servicesToCheck = ['nginx', 'docker']

    for servicesToCheck in servicesToCheck:
        p =  subprocess.Popen(["systemctl", "is-active",  servicesToCheck], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')

        print (output)

    if output != "active":
        print ("Check o servico", servicesToCheck)
    else:
    	print ("Servicos ativos")


servicesToCheck()