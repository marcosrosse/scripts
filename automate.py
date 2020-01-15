import subprocess

# ## Preparando e instalando pacotes necessarios

# subprocess.run(["apt-get", "update", "-y"])
# subprocess.run(["apt-get", "upgrade", "-y"])
# subprocess.run(["apt-get", "install", "nginx", "-y"])
# subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
# subprocess.run(["sh", "get-docker.sh"])

# # ## Checando se os serviços estão com status active

# def servicesToCheck():
#     services = ['docker', 'nginx']

#     for service in services:
#         process =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
#         (output, err) = process.communicate()
#         output = output.decode('utf-8')
        

#         if 'inactive' in output:
#             print("Os seguintes serviços estão desativos:", service)
#             # try:
#             #     trying = subprocess.Popen(["systemctl", "start", service], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#             # except:
#             #     print("O serviço:", trying, "falhou a inciar")
#         else:
#             print("Serviço:", service,"ativo")

# servicesToCheck()

## Criando e exportando arquivos de virtualhosts do nginx

def touchVirtualHosts():
    fileName = ['app1.conf', 'app2.conf', 'app3.conf']
    locationConfdNginx = '/home/mrossemo/'
    confFilesNginx =("server{\nlisten 80;\nserver_name app1.dexter.com.br; location /{\nproxy_pass http://10.215.47.45:8080/;\n}\n}",
     "server{\nlisten 80;\nserver_name app2.dexter.com.br; location /{\nproxy_pass http://10.215.47.45:8081/;\n}\n}",
      "server{\nlisten 80;\nserver_name app3.dexter.com.br; location /{\nproxy_pass http://10.215.47.45:8082/;\n}\n}")     
    for touching, config in zip (fileName, confFilesNginx):
        with open(locationConfdNginx + touching, 'w+') as file:
            file.writelines(config)

touchVirtualHosts()
    # subprocess.run(["rm", "-f", locationConfdNginx,"default.conf"])