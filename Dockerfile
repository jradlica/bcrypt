# Dockerfile
FROM python:3.9-alpine

# Install necessary dependencies
RUN pip install bcrypt

# Copy the script into the Docker container
COPY bcrypt_generator.py /bcrypt_generator.py

# Set the entry point to run the script
ENTRYPOINT ["python3", "/bcrypt_generator.py"]
