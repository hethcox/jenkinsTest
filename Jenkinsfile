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
ls -R .
/var/jenkins_home/workspace/jenkinsTest_main/.local/bin/pytest /var/jenkins_home/workspace/jenkinsTest_main

'''
      }
    }

  }
  environment {
    HOME = '/var/jenkins_home/workspace/jenkinsTest_main'
  }
}