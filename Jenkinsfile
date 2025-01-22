pipeline {
    agent any
    tools {
        // Nom du scanner configuré dans Manage Jenkins > Global Tool Configuration
        sonarqube 'SonarScanner'
    }
    stages {
        stage("build") {
            steps {
                echo 'Building the application'
                // Ajoutez vos commandes de build ici, par exemple :
                // sh './gradlew build'
                // ou mvn clean package
            }
        }
        stage("test") {
            steps {
                echo 'Testing the application'
                // Ajoutez vos commandes de test ici
            }
        }
        stage("SonarQube Analysis") {
            steps {
                // Utilisation du scanner SonarQube
                withSonarQubeEnv('SonarQube') {
                    echo 'Running SonarQube analysis'
                    sh 'sonar-scanner'
                }
            }
        }
        stage("deploy") {
            steps {
                echo 'Deploying the application'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
