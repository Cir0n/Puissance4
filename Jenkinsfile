pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application'
                // Ajoutez vos commandes de build ici
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') { // Nom défini dans SonarQube servers
                    sh 'sonar-scanner'
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
