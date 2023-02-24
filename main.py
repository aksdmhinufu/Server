from fastapi import FastAPI, File, UploadFile, HTTPException
import requests

app = FastAPI()

# Define the endpoint for the speech-to-text API
@app.post('/speech-to-text')
async def speech_to_text(audio: UploadFile = File(...)):
    # Check that the file is an audio file
    if not audio.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="File must be an audio file")

    # Get the audio data from the request
    audio_data = await audio.read()

    # Make a POST request to the Hugging Face API
    url = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h-robust"
    headers = {"Authorization": "Bearer api_key"}
    response = requests.post(url, headers=headers, data=audio_data)

    # Get the transcription from the API response
    transcription = response.json()[0]['transcription']

    # Return the transcription as a JSON response
    return {'transcription': transcription}

@app.get('/')
async def index():
    return "Pass input to API"
