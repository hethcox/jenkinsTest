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
sudo pip3 install pytest
pytest
'''
      }
    }

  }
}