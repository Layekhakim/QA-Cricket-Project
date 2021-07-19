# DevOps Core Practical Project
## Cricket Players Generator
# 
#
* [Introduction](#Introduction) 
  * [Objectives & Project Proposal](#)
  * [Requirements](#)
* [Sofware Architecture](#architecture)
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

My project create a cricket player generator that predicts how many runs the player will score against a particular team which is defined in the routes file of service 2. The user will first connect to server 1 which will display the webpage, however before displaying the page, a GET request is made to service 2 & 3. The second service will then return a random player, and service 3 a random cricket team. Then a POST request is made to service 4 sending the random 'player' and'team' information obtained from the previous GET requests. Service 4 consists of various IF statements that assigns a player to a team that they will play against and returns an outcome of how many runs the cricket player will score against a particular team.


### Requirements

In order to achieve the brief and achieve the SFIA requirements, the following requirements must be achieved:

* Kanban board
* Relational database 
* Clear documentation 
* An application fully integrated using the feature branch model into a Version Control System (VCS). The VCS will be built through a CI server (Jenkins) and deployed to a cloud-based virtual machine. 
* When any change is made to the code it is pushed to the VCS, webhooks must be set up for the CI server to recreate and redeploy the application
* Containerisation: Docker
* Ansible playbook must be made that will provide the environment for the application to run.
* A reverse proxy must be set up to make the application accessible to the user(NGINX).

## Software Architecture
#
### Project Management
For the project tracking I used a Kanban board on Trello. Trello is relatively easy to use which is why i used this particular kanban board.















### Database Structure
I have included pictures of an ERD diagram showing the structure of the database aswell as the database shown in SQL.


