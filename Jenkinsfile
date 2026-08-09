pipeline {
  agent { label 'linux-amd64' }
  options { timestamps(); buildDiscarder(logRotator(numToKeepStr: '10')) }
  stages {
    stage('Agent attestation') {
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail
          test "$(uname -m)" = "x86_64"
          cat > build-attestation.json <<EOF
          {"build":"${BUILD_TAG}","node":"${NODE_NAME}","architecture":"$(uname -m)","commit":"${GIT_COMMIT:-manual}","timestamp":"$(date -u +%FT%TZ)"}
          EOF
          cat build-attestation.json
        '''
      }
    }
    stage('Policy check') {
      steps { sh 'test ! -f .env && echo "No local secrets in workspace"' }
    }
  }
  post {
    always { archiveArtifacts artifacts: 'build-attestation.json', fingerprint: true; deleteDir() }
  }
}
