pipeline {
  agent {
    docker {
      image 'continuumio/miniconda3'
    }

  }
  stages {
    stage('Unit Tests') {
      steps {
        sh '''echo $PATH+EXTRA
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