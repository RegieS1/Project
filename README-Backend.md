Human Detection Backend API Documentation
------------------------------------------------------------------

This backend API provides an endpoint for human detection in images using Histogram of Oriented Gradients (HOG).

------------------------------------------------------------------
CREATE A PROJECT STRUCTURE:

Organize the folder and file
Example:

![image](https://github.com/RegieS1/Project/assets/146498517/eec62dd8-62a7-4b52-9aea-cee51ab4a8aa)

------------------------------------------------------------------
API ENDPOINT:

This endpoint processes images for human detection.

Endpoint URL: '/human_detection'
Method: POST

-----------------------------------------------------------------
PAYLOAD FORMAT:

Method: POST
Content-Type: multipart/formdata
Parameter: 'file' (type: file) - Upload an image file (JPEG, PNG, or JPG).

----------------------------------------------------------------
RESPONSE:

- Success:
  - Status Code: 200
  - Content-Type: application/json
  - Body: JSON response with the processed image URL in base64 format.

    Example:
    json
    {
      "result": "data:image/jpeg;base64,/4F/QSQSkZ..."
    }
   
- Error:
  - Status Code: 500
  - Content-Type: application/json
  - Body: JSON response with an error message.

    Example:
    json
    {
      "error": "An error occurred during image processing."
    }
    

----------------------------------------------------------------
HOW TO USE THE API:

run this command in the project directory


to run:
docker-compose up --build

To exit: short key - Ctrl+c
	or
docker-compose down


After building the image of backend and frontend, 

COPY the URL in your web browser  http://localhost:5001/ to send a POST request to /human_detection endpoint

----------------------------------------------------------------
DEPENDENCIES:

- [Flask](https://pypi.org/project/Flask/)
- [Flask-CORS](https://pypi.org/project/Flask-CORS/)
- [Pillow](https://pypi.org/project/Pillow/)
- [OpenCV](https://pypi.org/project/opencv-python/)

Notes
-----
You can't access the endpoint of the backend directly for the reason
that this is a POST method which is you need to upload the image and submit in the frontend.

Ensure the uploaded image is in JPEG, PNG, or JPG format.

The processed image URL is returned in base64 format for display in the frontend.
