#!/bin/bash

scp -i ~/id_rsa docker-compose.yaml qa@instance-1:/home/qa/docker-compose.yaml

#docker stack deploy
ssh -i ~/.ssh/id_rsa  qa@instance-1 << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml cricket_project
EOF