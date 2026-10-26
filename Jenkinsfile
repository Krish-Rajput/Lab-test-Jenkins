pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Fetches code from GitHub SCM
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                // Use 'bat' instead of 'sh' for Windows environments
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install beautifulsoup4'
                bat 'python test_form.py'
            }
        }
    }
}