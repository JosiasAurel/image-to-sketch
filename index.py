import cv2
from flask import Flask, request

app = Flask(__name__)


@app.route("/create/", methods=["POST"])
def handle_create():
    if "file" not in request.file:

        return {
            "Error": "File not found"
        }
    return "Created"


image_file = "flower.jpeg"

image = cv2.imread(image_file)


sketch_gray, sketch_color = cv2.pencilSketch(
    image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

# The below code is used in case you are running on your local envireonment
""" cv2.imshow("Pencil Sketch", sketch_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
 """
