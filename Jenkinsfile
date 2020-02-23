pipeline {

  agent any

    stages {

      stage('INSTALL DEPENDENCIES') {
       steps {
       sh 'pip install --upgrade jsondata'
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
          sh 'python3 -m twine upload dist/* -u keysafe'
        }
       }

      stage('DEPLOY') {
        steps {
          sh 'pip install --upgrade keysafe'
        }
       }

      }

/*      stage('DOCKER: Push image') {
        steps('push image') {
          sh 'docker push vipervit/keysafe:latest'
        }
      }
*/

    }
}
