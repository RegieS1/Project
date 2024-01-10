#import necessary libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import cv2
import numpy as np
import imutils

#Define paths for the MobileNetSSD model
protopath = "models/MobileNetSSD_deploy.prototxt"
modelpath = "models/MobileNetSSD_deploy.caffemodel"

#Read the MobileNetSSD model from the specified paths
net = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

#Define classes for detection (MobileNetSSD classes)
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

#Create a Flask app
app = Flask(__name__)
CORS(app)

def detect_objects(image, net, classes):

    (H, W) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)
    net.setInput(blob)
    
    detections = net.forward()

    results = []
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])

            if classes[idx] == "person":
                #Scale the bounding box coordinates
                box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = box.astype("int")

                results.append({
                    'confidence': float(confidence),
                    'box': [int(startX), int(startY), int(endX), int(endY)]
                })

    return results

@app.route('/human_detection', methods=['POST'])
def human_detection():
    try:
        #Get the uploaded file from the request
        file = request.files['file']

        if file:
            #Read and preprocess the image for detection
            image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            image = imutils.resize(image, width=600)

            #Perform object detection using the detect_objects function
            results = detect_objects(image, net, CLASSES)

            #Process detection results and return the response
            if results:

                #Draw bounding boxes on the image
                for result in results:
                    bounding_box = result['box']
                    cv2.rectangle(image, (bounding_box[0], bounding_box[1]),
                                  (bounding_box[2], bounding_box[3]), (0, 255, 0), 2)

                #Convert the processed image to base64 and return the result
                _, buffer = cv2.imencode('.jpg', image)
                image_str = base64.b64encode(buffer).decode('utf-8')

                return jsonify({'result': f'data:image/jpeg;base64,{image_str}'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
