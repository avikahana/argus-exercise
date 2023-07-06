pipeline {
    agent any
    
    stages {
        stage('Build & Deploy') {
            steps {
                sh 'docker build -t get_info .'

                withAWS(credentials: 'avikahana-aws-jenkins-credentials', region: 'us-east-1') {
     
                    // Upload the output file to S3
                    sh 'docker run -v /tmp:/app get_info aws s3 cp /app/info.txt s3://avikahana/'
                 
                    // Docker tag and push the Docker image to ECR
                    sh 'docker tag get_info:latest avikahana-ecr/get_info:latest'
                    sh 'docker push avikahana-ecr/get_info:latest'
                }
            }
        }

        stage('Pull & Test') {
            steps {
                withAWS(credentials: 'avikahana-aws-jenkins-credentials', region: 'us-east-1') {
     
                    // Download the most recent artifact from S3
                    sh 'aws s3 cp s3://avikahana/info.txt .'
                
                    // Test whether the artifact is empty and print the results to the console output
                    sh 'cat info.txt'
                }
            }
        }
    }

    post {
        always {
            // Change permissions of /var/run/docker.sock
            script {
                sh 'chmod 777 /var/run/docker.sock'
            }
        }
    }
}
