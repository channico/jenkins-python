pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/nicodemus-aquariux/simple_python'
            }
        }
        stage('Set up Python environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest
                '''
            }
        }
    }
}
