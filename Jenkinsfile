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
                    -Dsonar.host.url=http://192.168.221.131:9000 \
                    -Dsonar.token=sqa_c87e281d3d988190c2e5ea2e3ccbfea591c7cea3
                    '''
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
