# Use the official python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the python script into the container
COPY requirements.txt /app/
COPY get_info.py /app/

# Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your Python script
CMD ["python", "/app/get_info.py"]

