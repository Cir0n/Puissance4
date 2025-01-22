pipeline {
    agent any
    tools {
        maven 'Maven'  // Nom de la configuration Maven dans Jenkins
    }
    environment {
        SONARQUBE_SERVER = 'SonarQube' // Nom défini dans SonarQube servers
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the repository...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application with Maven...'
                sh 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    sh '''
                    mvn sonar:sonar \
                    -Dsonar.projectKey=Jenkins \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.login=sqa_c87e281d3d988190c2e5ea2e3ccbfea591c7cea3
                    '''
                }
            }
        }
        stage('Quality Gate') {
            steps {
                echo 'Checking SonarQube Quality Gate...'
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
