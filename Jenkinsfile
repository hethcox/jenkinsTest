pipeline {
  agent {
    docker {
      image 'continuumio/miniconda3'
    }

  }
  stages {
    stage('Unit Tests') {
      steps {
        sh '''pwd
pip3 install pytest
pytest

'''
      }
    }

  }
  environment {
    HOME = '/var/jenkins_home/workspace/jenkinsTest_main'
  }
}