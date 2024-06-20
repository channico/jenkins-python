pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/nicodemus-aquariux/simple_python.git'
            }
        }
        stage('Set up Python environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --junitxml=reports/junit.xml
                '''
            }
        }
    }
    post {
        always {
            junit 'reports/**/*.xml'
        }
    }
}