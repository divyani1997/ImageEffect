from flask import request, jsonify, send_file
from flask_restful import Resource
import cv2
import numpy as np
import base64
import re


class sketch(Resource):
    def post(self):
        # Get json data from request
        req = request.json

        # decode base64 into np array
        nparray = np.frombuffer(base64.b64decode(req['Image'].encode('utf-8')), np.uint8)

        # decoded image
        img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

        # Gray scale image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Negative of image
        img_neg = 255 - gray

        if re.match('/negative', request.path):
            return sketch.encoding(img_neg)

        # Blur image
        img_blur = cv2.GaussianBlur(img_neg, ksize=(21, 21), sigmaX=0, sigmaY=0)

        # Blend image
        img_blend = cv2.divide(gray, 255 - img_blur, scale=256)

        # cv2.imwrite("C:\\Users\\divya\\Downloads\\baby.jpeg", cartoon)

        # converting back to base64
        # img_encode = cv2.imencode('.jpg', img_blend)[1]
        # images64 = base64.b64encode(img_encode).decode('utf-8')
        return sketch.encoding(img_blend)

    @classmethod
    def encoding(self, img):
        img_encode = cv2.imencode('.jpg', img)[1]
        images64 = base64.b64encode(img_encode).decode('utf-8')
        return jsonify({"data": images64})

