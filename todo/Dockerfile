# Use the official Python image from the Docker Hub
FROM python:3.12.0-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only the necessary files for installing dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the FastAPI app code into the container
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the FastAPI server using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
