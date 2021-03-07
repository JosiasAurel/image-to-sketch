import cv2
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/create/", methods=["POST"])
def handle_create():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file_ = request.files['file']
        if file_.filename == '':
            return redirect(request.url)
        if file_:
            image = cv2.imread(file_)
            sketch_gray, sketch_color = cb2.pencilSketch(file_, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
            return render_template("result.html", image=sketch_gray, image_c=sketch_color)
    return render_template("index.html")


image_file = "flower.jpeg"

image = cv2.imread(image_file)


sketch_gray, sketch_color = cv2.pencilSketch(
    image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

# The below code is used in case you are running on your local envireonment
""" cv2.imshow("Pencil Sketch", sketch_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
 """
