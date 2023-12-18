## FRONTEND DOCUMENTATION

This is the frontend application for human detection using Histogram of Oriented Gradients (HOG).

----------------------------------------------------------------
## CREATE A PROJECT STRUCTURE:

Organize the folder and file
Example:

![image](https://github.com/RegieS1/Project/assets/146498517/d0ebfc1e-f05e-4845-bc6c-890c1be13b61)

----------------------------------------------------------------
## HOW TO USE:

Build docker image:
```bash
docker build -t frontend-image .
```
Run docker container:
```bash
docker run -p 5001:5001 frontend-image .
```

Access the frontend:
Open your web browser and go to http://localhost:5001

----------------------------------------------------------------
## DEPENDENCIES:

- [Flask](https://pypi.org/project/Flask/)
- [requests](https://pypi.org/project/requests/)

----------------------------------------------------------------
## Notes:
 - You can upload image in the frontend, but return in error if you going to submit, for the reason that you can only access the GET request method which only retrieve the data.
 - Displaying the result of the uploaded image needs the /human_detection endpoint of backend to process the image and return to frontend to displayed. 




 
