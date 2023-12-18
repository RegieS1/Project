# Import necessary libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
from io import BytesIO
from PIL import Image
import base64
import cv2
import numpy as np

#Create a Flask app
app = Flask(__name__)
CORS(app) #Enable CORS for the entire Flask app

#Define a route for processing images. This route handles POST requests.
@app.route('/human_detection', methods=['POST']) 

#This function handles requests to the /human_detection route.
def human_detection(): 
    """
    Endpoint for human detection in images using Histogram of Oriented Gradients (HOG).

    Payload:
        - POST request with a file upload containing an image (JPEG, PNG, or JPG).

    Returns:
        - JSON response with the processed image URL in base64 format.
        - If an error occurs during processing, returns a JSON response with an error message and status code 500.
    """

    try: 
        #Retrieve the uploaded image from the request
        file = request.files['file']

        #Check if a file was received in the request
        if file:

            #Open the image from the file and create an Image object
            image =Image.open(BytesIO(file.read())) 
            
            #Convert the Image to a NumPy array
            image_array =np.array(image)

            #Convert the image to grayscale
            gray_image =cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

            #Create a HOG descriptor
            hog =cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            
            #Apply HOG for detection
            boxes, weights =hog.detectMultiScale(gray_image, winStride=(8, 8), padding=(8, 8), scale=1.1)

            #Draw rectangles around detected objects in the image
            for (x, y, w, h) in boxes:
                cv2.rectangle(image_array, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            #Create a BytesIO object to store the annotated image in buffered variable.   
            buffered =BytesIO()
            
            #Convert and save annotated image to buffer
            Image.fromarray(image_array).save(buffered, format="JPEG") 
            
            #Convert the annotated image to base64 format for display in the frontend
            image_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

            #Return a JSON response with the annotated image URL
            return jsonify({'result': f'data:image/jpeg;base64,{image_str}'}) 
        
    # Handle exceptions and return an error response
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
