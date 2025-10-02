FROM python:3.13

# Set working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the contents of the current local directory into the container's working directory
COPY . /usr/src/app

# Run a command
CMD ["python", "hello.py"]