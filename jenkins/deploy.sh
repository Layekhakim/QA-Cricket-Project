#!/bin/bash
#copy over compose yaml to worker node
ssh -i ~/.ssh/ansible_id_rsa jenkins@manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    "docker stack deploy --compose-file docker-compose.yaml cricket_project"
EOF 
    docker stack deploy --compose-file docker-compose.yaml cricket_project
EOF