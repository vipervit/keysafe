pipeline {

  agent any

    stages {

      stage('INSTALL DEPENDENCIES') {
       steps {
       sh 'pip install --upgrade psutil'
       }
     }

      stage('TEST') {
        steps {
          sh 'pytest'
        }
      }

      stage('BUILD') {
        steps {
          sh 'rm -r -f dist'
          sh 'python3 setup.py sdist'
       }
      }

      stage('UPLOAD') {
        steps {
          sh 'python3 -m twine upload dist/* -u vipervit'
        }
       }

      stage('DEPLOY') {
        steps {
          sh 'pip install --upgrade viperlib'
        }
       }

      }

      stage('DOCKER: Push image') {
        steps('push image') {
          sh 'docker push vipervit/viperlib:latest'
        }
      }


    }
}
