
from flask import Flask, request, jsonify
import torch
from transformers import pipeline

app = Flask(__name__)

model_name = "distilgpt2"
generator = pipeline('text-generation', model=model_name)

def generate_text_inference(input_text, max_length=50):
    with torch.no_grad():
        result = generator(input_text, max_length=max_length)
    return result

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    input_text = data['text']
    max_length = data.get('max_length', 50)
    response = generate_text_inference(input_text, max_length)
    return jsonify(response[0]['generated_text'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
