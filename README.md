# SETTING UP FOR AUTOMATED TESTING

## Set up Jenkins
### Docker Image

Run this command:
```console
docker build -t qa-jenkins:latest .
```
This will install into the docker image
* latest version of python
* latest version pip
* Allure commandline

### Jenkins Plugins
* Install **ShiningPanda** plugin
* Install **Allure** plugin

### Python Packages
* pytest-html
* selenium

## Set up Selenium Grid
```console
docker-compose up -d
```
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


