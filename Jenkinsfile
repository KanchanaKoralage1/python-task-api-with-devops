pipeline{
    agent any
    environment{
        IMAGE="kanchana20/taskapi"
        TAG = "v${env.BUILD_NUMBER}"   // auto versioning
        KUBE_NAMESPACE = "taskapi"
        DEPLOYMENT_NAME = "task-api-deployment"
        CONTAINER_NAME = "taskapi"
    }

    stages{
        stage('Checkout') {
            steps {
                checkout scm   
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t $IMAGE:$TAG ./backend'
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
        stage('Deploy to Kubernetes') {
            steps {
                sh """
                kubectl set image deployment/${DEPLOYMENT_NAME} \
                ${CONTAINER_NAME}=${IMAGE}:${TAG} -n ${KUBE_NAMESPACE}
                """
            }
        }
    }
}