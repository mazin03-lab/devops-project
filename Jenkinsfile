pipeline {
    agent any

    environment {
        IMAGE_NAME = 'mazin03-lab/devops-app:1.0'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python -m pytest -v
                '''
            }
        }

        stage('Build & Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login \
                            --username "$DOCKERHUB_USER" \
                            --password-stdin

                        docker build -t "$IMAGE_NAME" .
                        docker push "$IMAGE_NAME"

                        docker logout
                    '''
                }
            }
        }
    }
}
