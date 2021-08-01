pipeline {
  agent {
    docker {
      image 'continuumio/miniconda3'
    }

  }
  stages {
    stage('Unit Tests') {
      steps {
        sh '''pip install pytest
/var/jenkins_home/workspace/jenkinsTest_main/.local/bin/pytest'''
      }
    }

  }
  environment {
    HOME = '/var/jenkins_home/workspace/jenkinsTest_main'
    PYTHONPATH = '/var/jenkins_home/workspace/jenkinsTest_main'
  }
}