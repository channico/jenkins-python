pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                cleanWs()
                git branch: 'main', url: 'https://github.com/channico/jenkins-python.git'
            }
        }
        stage('Set up Python environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pip install allure-pytest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --junitxml=reports/junit.xml --alluredir=reports/allure-results
                '''
            }
        }
    }
    post {
        always {
            junit 'reports/**/*.xml'
            allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
        }
    }
}