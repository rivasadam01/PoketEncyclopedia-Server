from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
import json
import requests
import logging
from collections import deque
import time


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Add this: Rolling average response time
response_times = deque(maxlen=5)


def process_image(img):
    global response_times
    start_time = time.time()
    with open('payload.json', 'r') as f:
        payload = json.load(f)
    payload['image_data'] = [{"data": img, "id": 12}]
    # Process the image
    result = requests.post("http://localhost:8888/completion", json=payload)

    try:
        json_response = result.json()
        print("Status Code:", result.status_code)
        response = json_response['content']
        end_time = time.time()
        response_time = end_time - start_time
        response_times.append(response_time)
        avg_response_time = sum(response_times) / len(response_times)
        print(f"Average response time: {avg_response_time}")
        return response, response_time, avg_response_time
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON response")
        return "Error: AI failed to process the image", None, None


@app.route('/get_response_time', methods=['GET'])
def get_response_time():
    try:
        avg_response_time = sum(response_times) / len(response_times)
        return jsonify({'avg_response_time': avg_response_time})
    except Exception as e:
        return jsonify({'avg_response_time': 21}), 200


@app.route('/process_image', methods=['POST'])
def handle_process_image():
    print(f"Process image request received")
    data = request.json
    base64_image = data['image']

    import base64
    from io import BytesIO
    from PIL import Image
    import os

    # Create a directory to store the images if it doesn't exist
    if not os.path.exists('captured_images'):
        os.makedirs('captured_images')

    # Decode the base64 string
    image_data = base64.b64decode(base64_image)

    # Open the image using PIL
    image = Image.open(BytesIO(image_data))

    # Generate a unique filename
    filename = f"captured_image_{int(time.time())}.jpg"
    filepath = os.path.join('captured_images', filename)

    # Save the image as JPG
    image.save(filepath, 'JPEG')

    print(f"Image saved as {filepath}")

    # Process the image
    response, response_time, avg_response_time = process_image(base64_image)

    return jsonify({
        'response': response,
        'image': base64_image,
        'response_time': response_time,
        'avg_response_time': avg_response_time
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
