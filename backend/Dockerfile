#backend/Dockerfile

#Use the official Python image as the base image
FROM python:3.12-slim

#Set the working directory inside the container
WORKDIR /app

#Copy the backend.py file to the container
COPY backend.py .

#Install dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0

#Install OpenCV dependencies
RUN apt-get install -y libsm6 libxext6 libxrender-dev

#Install Python packages
RUN pip install opencv-python flask Flask-CORS \ 
    pip install flask pillow

#Specifies the command to run when the container starts
CMD ["python", "backend.py"]
