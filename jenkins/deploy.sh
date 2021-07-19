#!/bin/bash
#copy over compose yaml to worker node
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@worker:/home/jenkins/docker-compose.yaml

#docker stack deploy
ssh -i ~/.ssh/id_rsa docker-compose.yaml jenkins@worker << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml cricket_project
EOF