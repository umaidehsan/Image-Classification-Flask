from __future__ import division, print_function
import os
import numpy as np
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# ✅ Path to your trained model
MODEL_PATH = 'model_resnet.h5'

# ✅ Load your trained model
model = load_model(MODEL_PATH)

# ✅ Image preprocessing and prediction function
def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='caffe')  # for ResNet50
    preds = model.predict(x)
    return preds

# ✅ Main route — open your index.html
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# ✅ Prediction route
@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    f = request.files['file']
    basepath = os.path.dirname(__file__)
    upload_folder = os.path.join(basepath, 'uploads')
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, secure_filename(f.filename))
    f.save(file_path)

    # Predict
    preds = model_predict(file_path, model)
    pred_class = decode_predictions(preds, top=1)
    result = str(pred_class[0][0][1])  # predicted class name
    return result

if __name__ == '__main__':
    # ✅ Run Flask app
    app.run(debug=True)
