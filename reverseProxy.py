import os
import os.path
import shutil
import subprocess
import sys


## Preparing environment and installing packages
def preparing():
    apps = ("ngnix docker-ce docker-ce-cli containerd.io")
    subprocess.run(["apt-get", "update", "-y"])
    subprocess.run(["apt-get", "upgrade", "-y"])
    process =  subprocess.Popen(["apt", "list", "--installed",  apps], stdout=subprocess.PIPE)
    (output, err) = process.communicate()
    output = output.decode('utf-8')

       
    if apps in output:
       return servicesToCheck
    else:    
        subprocess.run(["apt-get", "install", "nginx", "-y"])
        subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
        subprocess.run(["sh", "get-docker.sh"])
        os.remove("get-docker.sh")


## Checking services status
def servicesToCheck():
    services = ['docker', 'nginx']
    for service in services:
        process =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
        (output, err) = process.communicate()
        output = output.decode('utf-8')

        if 'inactive' in output:
            print("This services are inactives:", service, "... starting...")
            subprocess.Popen(["systemctl", "start", service])




## Creating and exporting nginx virtualhosts
def touchVirtualHosts():
    pathNgnix = '/etc/nginx/conf.d/'
    configFiles = ['app1.conf', 'app2.conf', 'app3.conf']
    configContents =(
    "server{\nlisten 80;\nserver_name app1.example.hi; location /{\nproxy_pass http://127.0.0.1:8080/;\n}\n}",
    "server{\nlisten 80;\nserver_name app2.example.hi; location /{\nproxy_pass http://127.0.0.1:8081/;\n}\n}",
    "server{\nlisten 80;\nserver_name app3.example.hi; location /{\nproxy_pass http://127.0.0.1:8082/;\n}\n}"
    )

    for configFile, config in zip(configFiles, configContents):
        with open(os.path.join(pathNgnix, configFile), 'w+') as file:
            file.write(config)



## Creating folder hierarchy 
def structureDocker():
    containers = ['app1', 'app2', 'app3']
    ports = ['8080', '8081', '8082']

    for container in containers:
        pathToRemove = os.path.join("/var/www/html/", container)

        if os.path.isdir(pathToRemove):
            shutil.rmtree(pathToRemove)
           
        newdir = '/var/www/html/{}/public_html/'.format(container)
        os.makedirs(newdir)
        
        with open(os.path.join(newdir, 'index.html'), 'w+') as file:
            file.write(container)
    
    for container, port in zip (containers, ports):
        executeDocker = ("docker run -dit --name {container} -p {port}:80 -v /var/www/html/{container}/public_html/:/usr/local/apache2/htdocs/ httpd:2.4".format(container=container, port=port))
        subprocess.call([executeDocker], shell=True)

def main():
    preparing()
    servicesToCheck()
    touchVirtualHosts()
    structureDocker()

if __name__ == '__main__':
    main()
