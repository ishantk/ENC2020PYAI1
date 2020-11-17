from flask import Flask
from flask import render_template
from flask import Response

import cv2

# pip install imutils
import imutils
from imutils.video import VideoStream

app = Flask("VIDEO STREAM APP")
video_stream = VideoStream(src=0).start()

@app.route('/')
def index():
    return render_template("vs-index.html")

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# this function will be a generator function which will yield frames :)
def generate_frames():
    while True:
        frame = video_stream.read()
        frame = imutils.resize(frame, width=600)
        (flag, encoded_image) = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n' b'Content-Type:image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')

if __name__ == '__main__':
    app.run(debug=True)


# Integration Activity
# Use the face_recognition library and check for the faces here :)

