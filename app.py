from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
# import your AI model libraries here

app = Flask(__name__)
CORS(app)  # allow cross-origin requests

# --- Load your AI model here ---
# Example: GPT-like model
# model = torch.load("path_to_model.pt")
# model.eval()

@app.route('/')
def index():
    return "AI API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # --- Run your model inference ---
    # Example:
    # result = model.generate(text)

    # For now, just a placeholder
    result = f"Processed text: {text}"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
