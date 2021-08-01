pipeline {
  agent {
    docker {
      image 'continuumio/miniconda3'
    }

  }
  stages {
    stage('Unit Tests') {
      steps {
        sh '''whoami
pwd
pip install pytest
pytest

'''
      }
    }

  }
  environment {
    HOME = '/root'
  }
}