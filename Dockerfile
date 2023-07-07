# Use the official python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /var/jenkins_home

# Copy the python script into the container
COPY get_info.py .

# Define the command to run your Python script
ENTRYPOINT ["python", "get_info.py"]

VOLUME /var/jenkins_home