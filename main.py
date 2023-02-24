from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the endpoint for the speech-to-text API
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    # Get the audio data from the request
    audio_file = request.files['audio']
    audio_data = audio_file.read()

    # Make a POST request to the Hugging Face API
    url = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h-robust"
    headers = {"Authorization": "Bearer api_key"}
    response = requests.post(url, headers=headers, data=audio_data)

    # Get the transcription from the API response
    transcription = response.json()[0]['transcription']

    # Return the transcription as a JSON response
    return jsonify({'transcription': transcription})

@app.route('/')
def index():
    return "Pass input to API"
