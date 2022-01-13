import os
import json
import ssl
import yolo_detection

from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():  # put application's code here
    return 'HELLO'

@app.route('/test', methods=['GET', 'POST'])
def test():  # put application's code here
 if request.method == 'POST':

#   data = request.args['msg']
#   data += 'flask'

    print('GET IMAGE')

    return jsonify({
       'result': 'true'
   })

@app.route('/image', methods=['POST'])
def image():
    try:
        image_file = request.files['image']  # get the image

        # Set an image confidence threshold value to limit returned data
        threshold = request.form.get('threshold')
        if threshold is None:
            threshold = 0.5
        else:
            threshold = float(threshold)

        #image_object = Image.open(image_file)
        #first try
        image_object = image_file.read()
        objects = yolo_detection.detectObjects(image_object)
        #second try
        #objects = yolo_detection.detectObjects(image_object)
        if (objects['detections'] == 'No object detected'):
            return jsonify({
            'result': 'false'
            })
        else:
            return jsonify({
            'result': 'true'
            })

    except Exception as e:
        print('POST /image error: ', e)
        return e

if __name__ == '__main__':
    app.debug = True
    #app.run(host='10.200.31.31', ssl_context = ('private.pem', 'public.pem'))
    #app.run(host = '0.0.0.0')
    #app.run(host = '10.200.31.31', port = 5000, debug = True, threaded = False)
    app.run(host = '192.168.1.23', port = 3001, debug = True, threaded = True)