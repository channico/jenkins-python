# SETTING UP FOR AUTOMATED TESTING

## Set up Jenkins
### Docker Image

Run this command (one time only):
```console
docker build -t jenkins-python:latest .
```

This will install into the docker image
* latest version of python
* latest version pip

### Python Packages
* pytest-html
* selenium

## Set up Selenium Grid

Create containers
```console
docker-compose up -d
```
Click on jenkins container to get the password it should look something like this:

```console
2024-06-20 17:55:59
2024-06-20 17:55:59 Jenkins initial setup is required. An admin user has been created and a password generated.
2024-06-20 17:55:59 Please use the following password to proceed to installation:
2024-06-20 17:55:59
2024-06-20 17:55:59 9745877e35934f3b8060b86d46626a2b
2024-06-20 17:55:59
2024-06-20 17:55:59 This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
2024-06-20 17:55:59
```

1. Go to localhost:8080 and enter the password into the box
2. Install suggested plugins
3. Create your admin username/password, etc.

## Set Up Additional Jenkins Plugins
### Jenkins Plugins

1. From the Jenkins dashboard click **Manage Jenkins**
2. Click on **Available plugins**
3. Search for the following plugins
   * **ShiningPanda**
   * **Allure**
4. Then click on **Install**

### Configure Allure
1. From the Jenkins dashboard click on **Tools**
2. Scroll down to find **Allure Commandline installations**
3. Enter `allure` in the **Name** textbox
4. Check the **Install automatically** checkbox.
5. Click on the **Save** button at the bottom of the screen

### Configure Environment Variables for our code
1. From the Jenkins dashboard click on **Manage Jenkins**
2. Click on **System**
3. Scroll down to **Global Properties**
4. Select **Environment Variables**
5. Click **Add**
6. Enter ``SELENIUM_URL`` for **Name**
7. Enter ``http://selenium-hub:4444/wd/hub`` in **Value**
8. Click on **Save**

## Creating your first Jenkins job
1. From the Jenkins Dashboard click on **+ New Item** or **Create a job +**
2. Enter a name for the job like ``demo-build``
   * **NOTE:** Item name should not have spaces
3. Choose **Pipeline** as the type of job
4. Click **OK**
5. In the Configuration screen for the demo-build job scroll down to **Pipeline**
6. Paste the following into the script Text area:
```json
pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/nicodemus-aquariux/simple_python.git'
            }
        }
        stage('Set up Python environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pip install allure-pytest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --junitxml=reports/junit.xml --alluredir=reports/allure-results
                '''
            }
        }
    }
    post {
        always {
            junit 'reports/**/*.xml'
            allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
        }
    }
}
```
7. Click on **Build Now** to run the job

**NOTE:**
    * The first time the job runs, Jenkins will download and install Allure
    * If the job hangs, stop it and rerun the job


## Controlling Container Instances

Stop
```console
docker-compose stop
```
Start
```console
docker-compose start
```
To delete
```console
docker-compose down
```


