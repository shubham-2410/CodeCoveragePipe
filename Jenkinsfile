pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311;C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\Scripts'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Ensure Python and dependencies are installed
                bat '''
                    set PATH=%PYTHON_PATH%;%PATH%
                    pip show coverage
                '''
            }
        }

        stage('Run Tests and Collect Coverage') {
            steps {
                // Run unit tests and collect code coverage
                bat '''
                    set PATH=%PYTHON_PATH%;%PATH%
                    coverage run -m unittest discover
                    coverage xml -o coverage.xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token')
            }
            steps {
                // Run SonarQube analysis, including coverage data
                bat '''
                    set PATH=%PYTHON_PATH%;%PATH%
                    sonar-scanner -Dsonar.projectKey=LearnPipeline ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000 ^
                    -Dsonar.token=%SONAR_TOKEN% ^
                    -Dsonar.python.coverage.reportPaths=coverage.xml
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline successfully completed"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
