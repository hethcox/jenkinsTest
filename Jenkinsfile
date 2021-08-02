pipeline {
  agent {
    docker {
      image 'continuumio/miniconda3'
    }

  }
  stages {
    stage('Unit Tests') {
      steps {
        sh '''unset SUDO_UID SUDO_GID SUDO_USER 
conda env create -f environment.yml
#pip install pytest
/var/jenkins_home/workspace/jenkinsTest_main/.local/bin/pytest .

conda run -n docker_env /bin/bash -c'''
      }
    }

  }
  environment {
    HOME = '/var/jenkins_home/workspace/jenkinsTest_main'
    PYTHONPATH = '/var/jenkins_home/workspace/jenkinsTest_main:$PYTHONPATH'
  }
}