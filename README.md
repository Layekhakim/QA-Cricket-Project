# DevOps Core Practical Project
## Cricket Players Generator
# 
#
* [Introduction](#Introduction) 
  * [Objectives & Project Proposal](#)
  * [Requirements](#)
* [Software Architecture](#architecture)
  * [Project Management](#trello)
  * [Risk Assessment](#risk)
  * [Database Structure](#entity-relationship-diagram)
  * [Continuous Integration Pipeline](#CI)
* [Software Infrastructure](#softwareinfrastructure)
  * [Jenkins](#jenkins)
  * [Services](#SERVICES)
  * [Front-End](#FrontEnd)
* [Components In Detail](#components)
  * [Docker](#docker)
  * [Docker-compose](#docker-compose)
  * [Swarm](#Swarmconfig)

* [Testing](#Testing)
  * [Unit Testing](#Unittesting)
  * [Test Coverage](#testcoverage)
* [Future Improvements & Constraints](#FutureImprovementsandProblems)
* [Author](#Author)
* [Acknowledgements](#Acknowledgements)

## Introduction 
#

### Objectives & Project Proposal

This was an indidual project which involved creating a service-orientated architecture application which had to consist of four services. Service one is the fundamental service which is known as the front-end whereby the user will see which should render the Jinja2 templates that interacts with my application, as well as communicating with other services.

My project creates a cricket player generator that predicts how many runs the player will score against a particular team which is defined in the routes file of service 2. The user will first connect to server 1 which will display the webpage, however before displaying the page, a GET request is made to service 2 & 3. The second service will then return a random player, and service 3 a random cricket team. Then a POST request is made to service 4 sending the random 'player' and'team' information obtained from the previous GET requests. Service 4 consists of various IF statements that assigns a player to a team that they will play against and returns an outcome of how many runs the cricket player will score against a particular team.


### Requirements

In order to achieve the brief and achieve the SFIA requirements, the following requirements must be achieved:

* Kanban board
* Relational database 
* Clear documentation 
* An application fully integrated using the feature branch model into a Version Control System (VCS). The VCS will be built through a CI server (Jenkins) and deployed to a cloud-based virtual machine. 
* When any change is made to the code it is pushed to the VCS, webhooks must be set up for the CI server to recreate and redeploy the application
* Containerisation: Docker
* Ansible playbook must be written accordingly which will provide the environment for the application to run.
* A reverse proxy must be set up to make the application accessible to the user(NGINX).

## Software Architecture
#
### Project Management
For the project tracking I used a Kanban board on Trello. Trello is relatively easy to use which is why i used this particular kanban board.

![] https://imgur.com/RlSAIbo


I have included my risk assessment below

![]https://imgur.com/sZpj3os


### Database Structure
I have included pictures of an ERD diagram showing the structure of the database aswell as the database shown in SQL.

![]https://imgur.com/a/7OgbzKm


### Continuous Integration Pipeline
The image below shows how the CI pipeline is used for my project. I begin with my project management using Trello board, once I have pushed up my latest code to GitHub, this will trigger a webhook which I have added but could not get it to work. This then automatically starts the jenkins pipeline. First, the requirements are installed, then the tests are done. Then using Docker-compose, the images will be built for all servers and pushed on to Dockerhub. Jenkins will then use Ansible to configure external nodes, including installing Docker on them. Ansible also configures as a load balancer node.The user finally conects to the load balancer and recieves the web page.

![]https://imgur.com/a/Rf85MKA


## Software Infrastructure
#
### Jenkins 
Jenkins is a free and open source automation server. It helps automate software development related to building, testing, and deploying, facilitating continuous integration and deployment. 

For this project, the stages of the Jenkins pipeline is as follows: 
* Testing - Which produces coverage reports on the console
* Build and push images - Docker-compose is used to build the images and push them to Docker-Hub
* Ansible configuration - Allows us to configure several servers at once, including:
* * Installing necessary dependencies,initializing the swarm and connecting to worker nodes and Configures the NGINX server for load-balancing
* Deploy stack - Configures the web-application on the manager and worker nodes

Further details on these stages used in the Jenkins pipeline can be found in the jenkinsfile. Below, I have also included an image of how the build appears on jenkins.


![]https://imgur.com/a/ggAfPom

The project must include a minimum of 4 services as part of the MVP

### Front-end

![]https://imgur.com/a/QWYg8Xn

## Components in detail

### Docker
Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. These are defined inside my Dockerfile(s)

### Docker-compose
Docker compose is a tool that needs to be installed alongside docker. This tool automates the docker build process. 
By running docker-compose, you don't have to install or maintain the software on your local machine. Your entire local development environment can be checked into source control, making it easier for other developers to collaborate on a project. The services that are created inside this file will be in the same network allowing for for each service to communicate with one another. Below is a picture of my images being built on Dockerhub

![]https://imgur.com/a/IqKIJGs

### Swarm
The swarm manager, both workers and NGINX all run on seperate VM's on Google Cloud Platform. The way in which the swarm works:
- It starts with the manager, it pulls down the services and runs copies of them across to the workers
- This exists so that indivudual containers arent overloaded by heavy traffic and so that if either server or any container stops working the app will continue to run.
- Nginx then acts as a reverse proxy
- It also directs which tasks will be used for each user balancing the load and making sure the containers are distributed appropriately.

The image below shows a basic set up of the swarm. Once Ansible installs docker on both swarm-manager and swarm-worker nodes. It then intialises the swarm on the manager node and joins the worker nodes.

![]https://imgur.com/a/GQhCvCS

## Testing 
#
### Unit Testing
For my project I implemented unit testing in the application. I tested all services. Unit testing allows us to test whether each function reuturns an expected response. I got a test coverage of 100 percent


## Future Improvements & Constraints
#

One big problem I ran into was being limited to 4 instances in one location.This caused me major issues as I had to constantly switch between instances by stopping and starting them. This was very frustrating and held me back.

- My request was denied, which lead to further difficulties with the deployment of the whole project. Therefore, some oppurtunity costs had to be made with the test coverage as this problem made me prirotize more importants tasks such as deployment of the application via jenkins

# Author
#
- Layek Hakim
## Acknowledgements
#
- Luke Benson

- Harry Volker











### Database Structure
I have included pictures of an ERD diagram showing the structure of the database aswell as the database shown in SQL.


