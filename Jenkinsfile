pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Application Test') {
            steps {
                sh '''
                    python3 -m py_compile app/app.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t autoheal-monitoring:${BUILD_NUMBER} ./app
                '''
            }
        }

        stage('Docker Image Check') {
            steps {
                sh '''
                    docker image inspect autoheal-monitoring:${BUILD_NUMBER}
                '''
            }
        }

        stage('Kubernetes Validation') {
            steps {
                sh '''
                    kubectl apply --dry-run=client -f k8s/deployment.yaml
                    kubectl apply --dry-run=client -f k8s/service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo 'AutoHeal CI pipeline completed successfully.'
        }
        failure {
            echo 'AutoHeal CI pipeline failed. Check the failed stage.'
        }
    }
}
