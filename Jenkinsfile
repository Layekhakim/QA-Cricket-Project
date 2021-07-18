pipeline {
    agent any
    stages {
        stage('Install Requirements')
            steps {
                sh 'bash jenkins/install-requirements.sh'
        
        
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
                sh 'docker-compose build'
            }
        }
        stage('Push') {
            steps {
                // install docker and docker compose
                // docker-compose push
                sh 'docker-compose push'
            }
        }
        stage('Configuration Management (Ansible)') {
            steps {
                // install ansible on jenkins machine for the jenkins user
                // ansible-playbook -i inventory.yaml playbook.yaml
                sh 'echo config'
            }
        }
        stage('Deploy') {
            steps {
                // create swarm infrastucture
                // copy ove docker-compose.yaml
                // ssh: docker stack deploy --compose-file docker-compose.yaml cricket_project
                sh 'echo deploy'

            }
        }
    }
}