# frontend/Dockerfile

#Specifies the base image to use.
FROM python:3.12-slim

#Sets the working directory inside the container to /app.
WORKDIR /app

#Copies 'frontend.py' and the 'templates' directory into the container.
COPY frontend.py .
COPY templates templates

# Install Flask and requests
RUN pip install Flask requests

# Specifies the command to run when the container starts, which is to execute frontend.py.
CMD ["python", "frontend.py"]
