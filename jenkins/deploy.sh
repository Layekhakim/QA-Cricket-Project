#!/bin/bash
#copy over compose yaml to manager node
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@instance-1:/home/jenkins/docker-compose.yaml

#docker stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@instance-1 << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml cricket_project
EOF