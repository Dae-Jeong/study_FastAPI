#!/bin/bash

set -e  # Any subsequent commands which fail will cause the shell script to exit immediately

# Set default values
PROJECT_NAME="todo"
IMAGE_NAME="${PROJECT_NAME}-fastapi"
CONTAINER_NAME="${PROJECT_NAME}-fastapi-container"
DOCKERFILE_PATH="${PROJECT_NAME}/Dockerfile"
HOST_PORT=8000
CONTAINER_PORT=8000

# Function to display error message and exit
function error_exit {
    echo "$1" 1>&2
    echo "Showing container logs (if available):"
    docker logs $CONTAINER_NAME || echo "No logs available."
    exit 1
}


# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -p|--project-name)
        PROJECT_NAME="$2"
        shift # past argument
        shift # past value
        ;;
        *)
        # unknown option
        echo "Unknown option: $1"
        exit 1
        ;;
    esac
done

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
docker build -t $IMAGE_NAME -f $DOCKERFILE_PATH $PROJECT_NAME || error_exit "Failed to build Docker image."

# Run the Docker container in the foreground
echo "Running the Docker container..."
docker run --rm -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME $IMAGE_NAME || error_exit "Failed to run Docker container."

# If script reaches here, container was started successfully
echo "Docker container has been started successfully."
