# Use the official Jenkins image as the base
FROM jenkins/jenkins:lts

# Switch to the root user to install additional software
USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y maven && \
    apt-get clean

# Switch back to the Jenkins user
USER jenkins

