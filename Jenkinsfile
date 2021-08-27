node {
  agent { dockerfile true }
  stages {
    stage('Test') {
      steps {
        app.inside {
            sh 'echo "Tests passed"'
        }
      }
    }
  }
}
