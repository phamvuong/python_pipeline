pipeline {
    agent any

    triggers {
        pollSCM('')
    }

    options {
        skipDefaultCheckout(true)
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building dockerfile"
                sh  ''' docker build . -t phamlamvuong/jenkin_job:1.0.0
                    '''
            }
        }

        stage('Test') {
            agent {
                docker {
                    image "python:3.7"
                    args '--user 0:0 -v /var/lib/jenkins/workspace/python-pipeline-master:/root/pipeline'
                }
            }
            steps {
                echo "Pep8 style check"
                sh  ''' 
                        python -m pip install pycodestyle
                        pycodestyle /root/pipeline/main.py || true
                    '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy to production cluster.'
            }
        }
    }
}
