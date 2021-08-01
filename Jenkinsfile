pipeline {
  agent any
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