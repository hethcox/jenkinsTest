pipeline {
  agent {
    docker {
      image 'continuumio/miniconda3'
    }

  }
  stages {
    stage('Unit Tests') {
      steps {
        sh '''ls
pip3 install pytest
pytest
'''
      }
    }

  }
}