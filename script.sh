#!/bin/bash
cd /home/ubuntu/Proyecto_Final/DockerFiles/API/
sudo docker build -t imagenapi .
sudo docker run -t -d -p 5000:5000 -v volapi:/home/APP/ --name dockerapi imagenapi >> /home/ubuntu/Proyecto_Final/logs.txt
cd /home/ubuntu/Proyecto_Final/DockerFiles/DB/
sudo docker build -t imagendb .
sudo docker run -t -d -p 3000:3000 -v voldb:/home/APP/ --name dockerdb imagendb >> /home/ubuntu/Proyecto_Final/logs.txt
cd /home/ubuntu/Proyecto_Final/DockerFiles/FRONT/
sudo docker build -t imagenfront .
sudo docker run -t -d -p 8080:8080 -v volfront:/home/APP/ -v voltemplates:/home/APP/templates/ --name dockerfront imagenfront >> /home/ubuntu/Proyecto_Final/logs.txt
sudo docker ps >> /home/ubuntu/Proyecto_Final/logs.txt
