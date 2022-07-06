pipeline {
    agent any
    stages {
        stage('Initilization') {
            steps {
                git branch: 'main', url: 'https://github.com/markacruz/python-microservice'
            }
        }
        stage('Build') { 
            steps {
                sh 'docker build -t python-microservice:${BUILD_NUMBER} .'
            }
        }
        stage('Upload to AWS ECR') { 
            steps {
                
            }
        }
    }
}