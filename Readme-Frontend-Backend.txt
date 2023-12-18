How Data is Passed Between Frontend and Backend:


The user upload an image through the frontend interface using the file input in the HTML form. When the form is submitted, a POST request is made to the backend API endpoint http://backend:5000/human_detection using the request.post method. The file data is sent as part of the POST request using the files parameter, which contains a dictionary with the file content. The backend processes the image, performs human detection using HOG, and returns the processed image(Annotated image)  URL in base64 format. the frontend check if the response status code is 200, it parses the JSON response and extracts the process image(Annotated image) URL. The processed image URL is passed to the render_template function, and the result is displayed on the frontend.



-----------------------------------------------------
FRONTEND:

Provide clear instructions on building and running the Docker container.

Navigate to the directory containing the frontend code.

Open a terminal in that directory.

Build the Docker image for the frontend:

Command:docker build -t frontend-image .

This command uses the Dockerfile in the frontend directory to build a Docker image named frontend-image

Run the Docker container for the frontend:

command:docker run -p 5001:5001 frontend-image
This command starts the frontend container, mapping port 5001 on your host to port 5001 in the container.



-----------------------------------------------------
BACKEND:

Provide clear instructions on building and running the Docker container.

Navigate to the directory containing the BACKEND CODE.

Open a terminal in that directory.

Build the Docker image for the backend:
Command:docker build -t backend-image .
This command uses the Dockerfile in the backend directory to build a Docker image named backend-image

Run the Docker container for the backend:
command:docker run -p 5001:5001 backend-image
This command starts the backend container, mapping port 5000 on your host to port 5000 in the container.




Building and Running both Frontend and Backend simultaneously 
------------------------------------------------------------------
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
	       backend.py
	       Dockerfile

docker-compose.yml
--------------------------------------------------------

the docker-compose.yml file should should look like this.

version: '3'

sercive:
	frontend:
		build:
			context: ./frontend
		ports:
		-"5001:5001"
		depends_on:
		- backend

	backedn:
		build:
			context: ./backend
		ports:
		-"5000:5000"
	


Use this command to build and run the Docker container 
command:docker-compose up --build


To stop the docker container: 
command: docker-compose down

