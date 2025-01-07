from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import csv

app = Flask(__name__)
CORS(app)


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def find_result_from_csv(index):
    with open('artists.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == str(index):
                return row
    return None

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        model = load_model('resnet_art_recognition.h5')

        try:
            image = Image.open(file_path)
            image = image.resize((224, 224))
            img_array = np.expand_dims(np.array(image) / 255.0, axis=0)

            predictions = model.predict(img_array)
            max_index = int(np.argmax(predictions[0]))
            result_list = find_result_from_csv(max_index)

            return jsonify({
                'statusCode': 200,
                'body': {
                    'id': max_index,
                    'prediction': result_list
                }
            }), 200

        except Exception as e:
            return jsonify({'error': f"Processing error: {str(e)}"}), 500

    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
