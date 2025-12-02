from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/')
def index():
    return "Simple API is running!"

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     text = data.get('text', '')

#     if not text:
#         return jsonify({'error': 'No text provided'}), 400

#     # Placeholder logic, no AI model
#     result = f"Processed text: {text}"

#     return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
