#!/bin/bash
#copy over compose yaml to manager node
ssh -i ~/.ssh/id_rsa qa@manager:~/docker-compose.yaml << EOF
    export DATABASE_URI=${DATABASE_URI}
    "docker stack deploy --compose-file docker-compose.yaml cricket_project"
EOF 
    docker stack deploy --compose-file docker-compose.yaml cricket_project
EOF
