// pipeline {
//     agent any

//     environment {
//         PYTHON_PATH = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311;C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\Scripts'
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 // Checkout the code from your repository
//                 checkout scm
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 // Ensure Python and dependencies are installed
//                 bat '''
//                     set PATH=%PYTHON_PATH%;%PATH%
//                     pip install coverage
//                 '''
//             }
//         }

//         stage('Run Tests and Collect Coverage') {
//             steps {
//                 // Run unit tests and collect code coverage
//                 bat '''
//                     set PATH=%PYTHON_PATH%;%PATH%
//                     coverage run -m unittest discover
//                     coverage xml -o coverage.xml

//                     if exist coverage.xml (
//                         echo "Coverage report generated Successfully."
//                     ) else (
//                         echo "Error : Coverage report not found!"
//                         exit /b 1
//                     )
//                 '''
//             }
//         }

//         stage('SonarQube Analysis') {
//             environment {
//                 SONAR_TOKEN = credentials('sonarqube-token')
//             }
//             steps {
//                 // Run SonarQube analysis, including coverage data
//                 bat '''
//                     set PATH=%PYTHON_PATH%;%PATH%
//                     sonar-scanner -Dsonar.projectKey=LearnPipeline ^
//                     -Dsonar.sources=. ^
//                     -Dsonar.host.url=http://localhost:9000 ^
//                     -Dsonar.token=%SONAR_TOKEN% ^
//                     -Dsonar.python.coverage.reportPaths=coverage.xml
//                 '''
//             }
//         }
//     }

//     post {
//         success {
//             echo "Pipeline successfully completed"
//         }
//         failure {
//             echo "Pipeline failed"
//         }
//     }
// }


pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311;C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\Scripts'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Coverage Installation') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip show coverage
                '''
            }
        }

        stage('Run Unit Tests and Generate Coverage') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Running tests with coverage..."
                coverage run --source= tests/fibo_test.py
                coverage xml -o coverage.xml
                if exist coverage.xml (
                    echo "Coverage report generated successfully."
                ) else (
                    echo "Error: Coverage report not found!"
                    exit /b 1
                )
                '''
            }
        }

        stage('Ensure Correct Working Directory') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Current working directory: %cd%"
                dir
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token') // Accessing the SonarQube token stored in Jenkins credentials
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%

                              sonar-scanner
                              -Dsonar.projectKey=CodeCoveragePipe ^
                              -Dsonar.sources=. ^
                              -Dsonar.python.coverage.reportPaths=coverage.xml ^
                              -Dsonar.host.url=http://localhost:9000 ^
                              -Dsonar.token=%SONAR_TOKEN%
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
