#!/bin/bash

# Set variables
IMAGE_NAME="my-fastapi"
CONTAINER_NAME="fastapi-container"
HOST_PORT=8000
CONTAINER_PORT=8000

# Check if the container is running
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}\$"; then
    # Container is running, stop and remove it
    echo "Stopping the running container..."
    docker stop $CONTAINER_NAME
    echo "Removing the stopped container..."
    docker rm $CONTAINER_NAME
fi

# Build the Docker image (if needed)
echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

# Run the Docker container
echo "Running the Docker container..."
docker run -d -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME $IMAGE_NAME

# Check if the container started successfully
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}\$"; then
    echo "Docker container has been restarted successfully."
    echo "Showing container logs:"
    docker logs $CONTAINER_NAME
else
    echo "Failed to start Docker container."
fi