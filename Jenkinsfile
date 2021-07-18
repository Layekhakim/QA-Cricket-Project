pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        install = 'false'
        DATABASE_URI = credentials('DATABASE_URI')
    }
    stages {
        stage('Install Requirements') {
            steps {
                script{
                    if (env.install== 'false'){
                        sh 'bash jenkins/install-requirements.sh'
                    }
                }
            }    
        }
        
        
        stage('Test') {
            steps {
                // pytest
                // run for each service
                // produce cov reports
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Build') {
            steps {
                // install docker and docker compose
                // docker-compose build
                sh 'echo build'
            }
        }
        stage('Push') {
            steps {
                // install docker and docker compose
                // docker-compose push
                sh 'echo push'
            }
        }
        stage('Configuration Manegement (Ansible)') {
            steps {
                // install ansible on jenkins machine for the jenkins user
                // ansible-playbook -i inventory.yaml playbook.yaml
                // sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
                sh 'echo config'

            }
        }
        stage('Deploy') {
            steps {
                // create swarm insfrastucture
                // copy ove docker-compose.yaml
                // ssh: docker stack deploy --compose-file docker-compose.yaml cricket_project
                sh 'echo deploy'

            }
        }
    }
}