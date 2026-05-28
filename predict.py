from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask_cors import CORS
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load model
model = load_model("lung_cancer_with_unknown_model.h5")

# Labels
labels = ['Stage1', 'Stage2', 'Stage3', 'Normal', 'Unknown']

CONFIDENCE_THRESHOLD = 0.7

# HOME ROUTE
@app.route('/')
def home():
    return "LungVision API Running Successfully"

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

# PREDICT ROUTE
@app.route('/predict', methods=['POST'])
def predict():

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        img = preprocess_image(file.read())

        prediction = model.predict(img)

        max_prob = float(np.max(prediction))
        predicted_class = np.argmax(prediction)

        if max_prob < CONFIDENCE_THRESHOLD:
            label = "Unknown"
        else:
            label = labels[predicted_class]

        return jsonify({
            "label": label,
            "confidence": max_prob
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
