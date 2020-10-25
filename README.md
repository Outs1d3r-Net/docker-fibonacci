# Sequencia de fibonacci em python  
> Este documento é para atividade continua da materia de devops da faculdade impacta.  

## Primeiro instale o docker em seu ambiente:
```
$ nano install-docker.sh
```

```
#!/bin/bash
echo "Preparando..."
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
echo 'deb https://download.docker.com/linux/debian stretch stable' > /etc/apt/sources.list.d/docker.list
echo "Atualizando..."
apt-get -y update
apt-get -y remove docker docker-engine docker.io
echo "Instalando..."
apt-get -y install docker-ce
echo "Testando docker Hello World..."
docker run hello-world
```

```
$ sudo bash install-docker.sh
```  

## Depois realize a criação do docker apartir do dockerfile:  
```
$ git clone https://github.com/Outs1d34r-Net/docker-fibonacci.git
$ cd docker-fibonacci
$ sudo docker build -t nomequalquerparaminhaimage .
$ sudo docker run -p 5000:5000 -d nomequalquerparaminhaimage
```
> Acesse https://localhost:5000 em seu browser.  
