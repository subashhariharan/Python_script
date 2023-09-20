import cv2
import numpy as np
import json

# Load the YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load the COCO class labels
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Load the image
image = cv2.imread("image.jpg")
height, width = image.shape[:2]

# Create a blob from the image and set it as input to the network
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# Perform object detection
layer_names = net.getUnconnectedOutLayersNames()
outputs = net.forward(layer_names)

# Initialize lists to store object information
objects = []

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            objects.append({
                "class": classes[class_id],
                "confidence": float(confidence),
                "x": x,
                "y": y,
                "width": w,
                "height": h
            })

# Convert the results to JSON
result_json = json.dumps(objects, indent=4)

# Print or return the JSON
print(result_json)
