
Es necesario tener instalado docker, por lo tanto si no lo tiene instalado dentro de su maquina y usa ubuntu, es recomendable seguir las siguientes instrucciones: </br>
https://docs.docker.com/install/linux/docker-ce/ubuntu/ </br>
Adicionalmente en necesario contar tambien con docker-compose, si no lo tiene instalado, siga el siguiente tutorial. </br>
https://docs.docker.com/compose/install/ </br>

</br>
</br>
Para ejecutar la aplicación dockerizada es necesario seguir los siguientes pasos dentro de la terminal:
<ol>
  <li> Si tiene el proyecto en su maquina, acceda a la ubicacion del mismo por medio del comando CD, de lo contrario clonelo usando <b> sudo git clone https://github.com/lealdaniel00/gestionTecnologicaServicios.git </b> </li>
  <li> Acceda al la ubicacion del proyecto clonado por medio de <b>cd </b>  (cd gestionTecnologicaServicios)</li>
  <li> Correr el proyecto usando <b>sudo docker-compose up --build</b> </li>
  <li> desde el navegador acceda a la siguiente direccion </li>
  <li> http://0.0.0.0:5006/show_all </li>
  <li> podra <b>sumar, restar, dividir y multiplicar</b> dos numeros usando microservicios </li>
</ol>



# Python Calculator - Microservices
A simple calculator made in python, where each basic operation is a microservice that runs in a different Docker container. 

## Installation
It is necessary to have docker installed, therefore if you do not have it installed inside your machine and you use Ubuntu, it is advisable to follow the following instructions: </br>
https://docs.docker.com/install/linux/docker-ce/ubuntu/
You also need to install docker-compose. If you don't have it installed, take the following tutorial: </br>
https://docs.docker.com/compose/install/


To run the dockerized application, you have to execute the following steps inside the terminal:

```sh
git clone https://github.com/tdavilab/python-calculator-microservices.git
cd python-calculator-microservices
sudo docker-compose up --build
```

## Usage

Go to the browser and access the next address:
http://0.0.0.0:50006/show_all

You will be able to interact with the calculator, where each operation is running on a different container.

**Made by:**
Thomas Daniel Avila Blenkey, Jonathan Steven Capera Quintana and Daniel David Leal Lara
