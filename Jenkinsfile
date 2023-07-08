pipeline {
    agent any
    stages {
        stage('prepare') {
            steps {
                sh 'sudo usermod -aG docker jenkins'
                sh 'newgrp docker'
                sh 'sudo chmod 777 /var/run/docker.sock'

                sh """
                    sudo docker rm -f get_info || true
                    sudo docker image rm -f get_info || true
                """
            }
        }
        stage('Build & Deploy') {
            steps {
                echo 'Get repo from GitHub'
                git url: 'https://github.com/avikahana/argus-exercise.git', branch: 'main'
                sh('ls')
                sh('pwd')
                echo 'Build docker image from Dockerfile'
                sh 'sudo docker build -f Dockerfile -t get_info .'
                echo 'File list before docker run'
                sh('ls')
                sh('pwd')
                echo 'Run docker get_info'
                //sh 'docker run --group-add 0 --publish 8080:8080 --name get_info get_info'
                sh 'docker run --group-add 0 --publish 8080:8080 --name get_info --volume /var/run/docker.sock:/var/run/docker.sock get_info'
                echo 'file list after docker run'
                sh('ls')
                // withAWS(region:'us-east-1',credentials:'AWS-Access-Key') {
                //     //sh 'docker run --group-add 0 --publish 8080:8080 --name get_info --volume /var/run/docker.sock:/var/run/docker.sock get_info /bin/sh -c "ls"'
                //     sh ('ls')
                //     //    s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'info.txt', bucket:'avikahana')
                // }
            }
        }
    }
}
