README file explaining how to use your frontend, including any dependencies.
----------------------------------------------------------------
FRONTEND DOCUMENTATION

This is the frontend application for human detection using Histogram of Oriented Gradients (HOG).

----------------------------------------------------------------
CREATE A PROJECT STRUCTURE:

Organize the folder and file
Example:

Project/
	frontend/
		templates/
			index.html
		Dockerfile
		frontend.py
	backend/
	       ...

----------------------------------------------------------------
HOW TO USE:

Build docker image:
command:docker build -t frontend-image .

Run docker container:
command:docker run -p 5001:5001 frontend-image .

Access the frontend:
Open your web browser and go to http://localhost:5001

----------------------------------------------------------------
DEPENDENCIES:

- Flask
- Requests

----------------------------------------------------------------
Notes:
-You can upload image in the frontend, but return in error if you going to submit, for the reason that you can only access the GET request method which only retrieve the data. Displaying the result of the uploaded image needs the /human_detection endpoint of backend to process the image and return to frontend to displayed. 
- Ensure the backend service is running at `http://backend:5000`.




 