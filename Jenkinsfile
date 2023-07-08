#!/usr/bin/env bash

pipeline {

    agent any

    stages {
        stage('prepare') {
            when {
                anyOf {
                    environment name: 'RUN', value: 'Build & Deploy' 
                    branch 'master'
                }    
            }
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
            when {
                anyOf {
                    environment name: 'RUN', value: 'Build & Deploy' 
                    branch 'main'
                }    
            }
            steps {
                
                echo 'Pull files from a GitHub repository'
                git url: 'https://github.com/avikahana/argus-exercise.git', branch: 'main'

                echo 'Build docker image from Dockerfile'
                sh 'sudo docker build -f Dockerfile -t get_info .'
                
                
                echo 'Run docker get_info'
                sh 'sudo docker run --group-add 0 --publish 8080:8080 --name get_info --volume /var/run/docker.sock:/var/run/docker.sock get_info'
                
                // Temp step until shared folder from Docker inside Docker will be resolve
                // Only this left
                sh 'python3 get_info.py'
                
                withAWS(region:'us-east-1',credentials:'avikahana-aws-token') {

                    echo 'Upload the info.txt output file to S3 bucket'
                    s3Upload (acl: 'Private' , bucket: 'avikahana' , file: 'info.txt')
                    
                    echo 'Upload Docker image to AWS ECR'
                    sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 161192472568.dkr.ecr.us-east-1.amazonaws.com'
                    sh 'docker build -t avikahana .'
                    sh 'docker tag avikahana:latest 161192472568.dkr.ecr.us-east-1.amazonaws.com/avikahana:latest'
                    sh 'docker push 161192472568.dkr.ecr.us-east-1.amazonaws.com/avikahana:latest'
                }
            }
        }

        stage('Pull & Test') {
            when {
                anyOf {
                    environment name: 'RUN', value: 'Pull & Test' 
                    triggeredBy 'TimerTrigger'
                }    
            }
            steps {
                
                withAWS(region:'us-east-1',credentials:'avikahana-aws-token') {
                    echo 'Download the info.txt file from S3 bucket'
                    s3Download(file: 'downloaded_info.txt', bucket: 'avikahana', path: 'info.txt', force: true)
                }

                echo 'Validate if the downloaded file from S3 is not empty'
                script{
                    def output_list = readFile("downloaded_info.txt")
                    if (output_list.size() == 0) {
                        echo "Failed:: The file is empty!"
                    }
                    else {
                        echo "Success:: The file is NOT empty!"
                        sh 'cat downloaded_info.txt'
                    }
                }
            }
        }
    }

    post { 
        always { 
            cleanWs()
        }
    }
}
