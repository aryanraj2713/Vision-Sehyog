from flask import Flask, render_template, Response, send_from_directory
from camera import VideoCamera
import cv2
import numpy as np
import time
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.js')
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               

@app.route('/video_feed')
def video_feed():
    net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')

    class_names = []
    with open("coco.names", "r") as f:
        class_names = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(class_names), 3))

    cap = cv2.VideoCapture(0)
    starting_time = time.time()
    frame1_id = 0

    font = cv2.FONT_HERSHEY_PLAIN
    while True:
        _, frame1 = cap.read()
        height, width, channels = frame1.shape

        frame1_id += 1
        
        #------------------- Détecter les objets -------------------
        
        # On décompose la frame1 pour les 3 couleurs RVB 
        blob = cv2.dnn.blobFromImage(frame1, 0.009, (320, 320), (0, 0, 0), True, crop=False)
        
        net.setInput(blob)
        outs = net.forward(output_layers)
        
        #--------------- Information sur les objets ----------------
        
        class_ids = []
        confidences = []
        boxes = []
        
        for out in outs:
            
            for detection in out:
                
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > 0.5:
                    
                    # L'objet est maintenant détecté
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
                    
                    # cv2.circle(img, (center_x, center_y), 10, (0, 255, 0), 2)
        
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
        
        for i in range(len(boxes)):
            
            if i in indexes:
                
                x, y, w, h = boxes[i]
                label = str(class_names[class_ids[i]])
                confidence = confidences[i]
                color = colors[class_ids[i]]
                cv2.rectangle(frame1, (x,y), (x+ w, y + h), color, 2)
                cv2.putText(frame1, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3, color, 2, 3)
        
        time_past = time.time() - starting_time
        fps = frame1_id / time_past
        cv2.putText(frame1, "FPS: " + str(round(fps, 1)), (150, 50), font, 3, (0, 255, 0), 4)
        cv2.imwrite('./static/frame1.png',frame1)
        return send_from_directory(os.path.join(app.root_path, 'static'), 'frame1.png',
                           mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)