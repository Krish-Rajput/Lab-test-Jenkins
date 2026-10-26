pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Fetches code from GitHub repository
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                // Executes the automated test script
                sh 'python3 -m pip install beautifulsoup4'
                sh 'python3 test_form.py'
            }
        }
    }
}