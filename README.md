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

</br>
</br>

**Made by:**
Thomas Daniel Avila Blenkey, Jonathan Steven Capera Quintana and Daniel David Leal Lara
