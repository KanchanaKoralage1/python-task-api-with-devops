pipeline{
    agent any
    environment{
        IMAGE="kanchana20/taskapi"
        TAG = "${env.GIT_COMMIT.substring(0,7)}"   
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

        stage('Deploy to AKS') {
            steps {
                withCredentials([file(credentialsId: 'aks-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh """
                        kubectl set image deployment/${DEPLOYMENT_NAME} \
                            ${CONTAINER_NAME}=${IMAGE}:${TAG} \
                            -n ${KUBE_NAMESPACE}
                    """
                }
            }
        }

        stage('Rollout Status Check') {
            steps {
                withCredentials([file(credentialsId: 'aks-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh "kubectl rollout status deployment/${DEPLOYMENT_NAME} -n ${KUBE_NAMESPACE}"
                }
            }
        }
        // stage('Deploy to Kubernetes') {
        //     steps {
        //         sh """
        //         kubectl set image deployment/${DEPLOYMENT_NAME} \
        //         ${CONTAINER_NAME}=${IMAGE}:${TAG} -n ${KUBE_NAMESPACE}
        //         """
        //     }
        // }
        // stage('Rollout Status Check') {
        //     steps {
        //         sh "kubectl rollout status deployment/${DEPLOYMENT_NAME} -n ${KUBE_NAMESPACE}"
        //     }
        // }

    }
    post {
        failure {
            withCredentials([file(credentialsId: 'aks-kubeconfig', variable: 'KUBECONFIG')]) {
                sh "kubectl rollout undo deployment/${DEPLOYMENT_NAME} -n ${KUBE_NAMESPACE}"
            }
        }
    }
}