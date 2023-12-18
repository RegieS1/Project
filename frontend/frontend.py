#Import necessary libraries
from flask import Flask, render_template, request
import requests

#Create a Flask app
app = Flask(__name__)

#Define a route for the root URL (/). This route handles both GET and POST requests
@app.route('/', methods=['GET','POST'])  

#This function handles requests to the root URL
def index():

    """
    Endpoint for the index page.

    Handles both GET and POST requests. Displays the uploaded image and processed result.

    Returns:
        - Renders the 'index.html' template with the processed result.
    """
    #Initialize the result variable to None
    result = None  

    if request.method =='POST':

        #Access the uploaded file from the request. with the key "file"
        file = request.files['file'] 

        #Check if a file was received
        if file: 

            #Send the file to the backend for processing

            #Set the URL of the backend service where the file will be sent for processing
            backend_url='http://backend:5000/human_detection' 

            #Create a dictionary of files to be sent in the POST request
            files ={'file': file.read()}

            #Use the requests library to send a POST request to the backend with the file
            response =requests.post(backend_url, files=files) 

            #Check if the response status code is 200(success)
            if response.status_code == 200:

                 #Parse the JSON response from the backend and assign it to the result variable.
                result =response.json()

            else:
                print("Backend Error:",response.text)

    #Render the index.html template, passing the result variable to the template for display.
    return render_template('index.html',result=result)
    
# Run the Flask app
if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)


