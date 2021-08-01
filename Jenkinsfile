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
ls -R /var/jenkins_home/workspace/jenkinsTest_main/.local/bin/
/var/jenkins_home/workspace/jenkinsTest_main/.local/bin/pip install pytest
pytest

'''
      }
    }

  }
  environment {
    HOME = '/var/jenkins_home/workspace/jenkinsTest_main'
  }
}