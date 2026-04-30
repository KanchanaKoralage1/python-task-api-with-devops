pipeline{
    agent any
    environment{
        IMAGE="kanchana20/taskapi"
        TAG="V1"
    }

    stages{
        stage('Clone Repo'){
            steps{
                git 'https://github.com/KanchanaKoralage1/python-task-app.git'
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t $IMAGE:$TAG .'
            }
        }
        stage('Docker Login'){
            steps{
                withCredentials([usernamePassword(credentialId:'dockerhub-creds', usernameVariable:'USER', passwordVariable:'PASS')])
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