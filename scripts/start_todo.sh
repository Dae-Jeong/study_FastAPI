#!/bin/bash

set -e  # Any subsequent commands which fail will cause the shell script to exit immediately

# Set variables
IMAGE_NAME="todo-fastapi"
CONTAINER_NAME="todo-fastapi-container"
HOST_PORT=8000
CONTAINER_PORT=8000
DOCKERFILE_PATH="todo/Dockerfile"
PROJECT_PATH="todo"

# Function to display error message and exit
function error_exit {
    echo "$1" 1>&2
    echo "Showing container logs (if available):"
    docker logs $CONTAINER_NAME || echo "No logs available."
    exit 1
}

# Ensure the container is stopped and removed on exit
trap 'docker stop $CONTAINER_NAME || true && docker rm $CONTAINER_NAME || true' EXIT

# Check if the container is running
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}\$"; then
    # Container is running, stop and remove it
    echo "Stopping the running container..."
    docker stop $CONTAINER_NAME || error_exit "Failed to stop container."
    echo "Removing the stopped container..."
    docker rm $CONTAINER_NAME || error_exit "Failed to remove container."
fi

# Build the Docker image (if needed)
echo "Building the Docker image..."
docker build -t $IMAGE_NAME -f $DOCKERFILE_PATH $PROJECT_PATH || error_exit "Failed to build Docker image."

# Run the Docker container in the foreground
echo "Running the Docker container..."
docker run --rm -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME $IMAGE_NAME || error_exit "Failed to run Docker container."

# If script reaches here, container was started successfully
echo "Docker container has been started successfully."
