pipeline {
    agent any

    environment {
        // PostgreSQL environment variables
        DB_HOST = 'demo-postgress.c5su6s0e6hei.us-east-1.rds.amazonaws.com'
        DB_PORT = '5432' // default PostgreSQL port
        DB_NAME = 'demo-postgress'
        DB_USER = 'postgress'
        DB_PASSWORD = 'demopostgress'
        //DB_PASSWORD = credentials('postgres_password') // Jenkins credential ID
        //PYTHON_ENV = '/path/to/python' // Path to Python interpreter or virtual environment
        BRANCH = "develop"
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                // Checkout the repository from GitHub
                git branch: '${BRANCH}',
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/Mylavarap/Demo.git'
            }
        }
        // stage('Clone Repo') {
        //     steps {
        //         // Checkout the repository from GitHub
        //         sh 'rm -rf Demo'
        //         sh 'git clone -b ${BRANCH} git@github.com:Mylavarap/Demo.git'
        //     }
        // }

        stage('Install Python Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    // Assuming requirements.txt is in the root of the repo
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                    '''
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Run the Python script to update PostgreSQL
                    sh '''
                        . venv/bin/activate
                        python3 update_postgress_db.py --db-user ${DB_USER} --db-pass ${DB_PASSWORD} --db-host ${DB_HOST} --db-name ${DB_NAME} --db-port ${DB_PORT}
                    '''
                }
            }
        }
    }

    post {
        always {
            // Cleanup virtual environment
            sh 'rm -rf venv'
        }
        success {
            echo 'Pipeline executed successfully. Python script ran, and the database was updated.'
        }

        failure {
            echo 'Pipeline failed. Check the logs for errors.'
        }
    }
}
