#!groovy

pipeline {
    agent any
    stages {
        stage('prepare') {
            steps {
                sh 'sudo usermod -aG docker jenkins'
                sh 'newgrp docker'
                sh 'sudo chmod 777 /var/run/docker.sock'
                // sh 'docker rm --force get_info'

                sh """
                    sudo docker rm -f get_info || true
                    sudo docker image rm -f get_info || true
                """
            }
        }
        stage('Build & Deploy') {
            steps {
                echo 'Get some code from a GitHub repository'
                git url: 'https://github.com/avikahana/argus-exercise.git', branch: 'main'
                sh('ls')
                sh('pwd')
                sh 'sudo docker build -f Dockerfile -t get_info .'
                sh('ls')
                sh('docker ps')

                withAWS(region:'us-east-1',credentials:'AWS-Access-Key') {

                    sh 'docker run --group-add 0 --publish 8080:8080 --name get_info --volume /var/run/docker.sock:/var/run/docker.sock get_info /bin/sh -c "ls"'
                    //sh 'docker run --group-add 0 --publish 8080:8080 --name get_info --volume /var/run/docker.sock:/var/run/docker.sock get_info /bin/sh -c "ls"'

                    sh ('ls')
                    //    s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'info.txt', bucket:'avikahana')
                }
            }
        }
    }
}
