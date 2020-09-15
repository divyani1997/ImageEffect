import io

from flask import request, jsonify, send_file
from flask_restful import Resource
import cv2
import numpy as np
import base64


class cartoon(Resource):
    def post(self):
        # Get json data from request
        req = request.json

        # decode base64 into np array
        nparray = np.frombuffer(base64.b64decode(req['Image'].encode('utf-8')), np.uint8)

        # decoded image
        img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

        # Edges
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        # cartoonization
        color = cv2.bilateralFilter(img, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        # cv2.imwrite("C:\\Users\\divya\\Downloads\\baby.jpeg", cartoon)

        # converting back to base64
        img_encode = cv2.imencode('.jpg', cartoon)[1]
        images64 = base64.b64encode(img_encode).decode('utf-8')
        return jsonify({'message': "hi", "data": images64})
