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
pip install -r requirements.txt
pytest

'''
      }
    }

  }
  environment {
    HOME = '/root'
  }
}