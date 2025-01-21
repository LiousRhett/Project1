# Use an official Python runtime as a parent image
FROM python:3.13-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN uv pip compile pyproject.toml -o requirements.txt && pip install --no-cache-dir -r requirements.txt

# Expose port for the API server
EXPOSE 80

# Run the command to start the API server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:create_app"]
