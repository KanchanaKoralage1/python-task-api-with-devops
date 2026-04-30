pipeline{
    agent any
    environment{
        IMAGE="kanchana20/taskapi"
        TAG="V1"
    }

    stages{
        stage('Checkout') {
            steps {
                checkout scm   // <-- add this
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t $IMAGE:$TAG .'
            }
        }
        stage('Docker Login'){
            steps{
                withCredentials([usernamePassword(credentialsId:'dockerhub-creds', usernameVariable:'USER', passwordVariable:'PASS')])
                {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }
        stage('Push Image'){
            steps{
                sh 'docker push $IMAGE:$TAG'
            }
        }
    }
}