pipeline {
    agent any
    stages {
        stage('Initilizing') {
            steps {
                git branch: 'main', url: 'https://github.com/markacruz/python-service'
            }
        }
        stage('Building Dockerfile') { 
            steps {
                sh 'docker images prune'
                sh 'docker build -t python-service:${BUILD_NUMBER} .'
            }
        }
        stage('Uploading to ECR') {
            steps {
                sh """
                /usr/local/bin/aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 513339161784.dkr.ecr.us-east-1.amazonaws.com
                docker images
                docker tag python-service:${BUILD_NUMBER} 513339161784.dkr.ecr.us-east-1.amazonaws.com/python-service
                docker push 513339161784.dkr.ecr.us-east-1.amazonaws.com/python-service
                """
            }
        }
        stage('Updating Lambda Function') {
            steps {
                sh """
                /usr/local/bin/aws lambda update-function-code \
                --function-name python-service \
                --image-uri 513339161784.dkr.ecr.us-east-1.amazonaws.com/python-service:latest
                """   
            }
        }
        stage('Updating HTTP Gateway') {
            steps {
                sh """
                aws apigatewayv2 create-api --name python-service-api \
                --protocol-type HTTP \
                --target arn:aws:lambda:us-east-1:513339161784:function:python-service
                """
            }
        }
    }
}
