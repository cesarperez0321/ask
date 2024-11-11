import openai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

openai.api_key = "sk-proj-c3V6jLr8MltEyY3TdHfIT3BlbkFJqsrUf6TaKuwBrafWaFjS"  # Coloca tu clave API aquí

app = Flask(__name__)
CORS(app)

@app.route('/speech_to_speech', methods=['POST'])
def speech_to_speech():
    audio_file = request.files['audio']
    audio_content = audio_file.read()

    # Paso 1: Convierte el audio a texto usando Whisper
    try:
        transcription = openai.Audio.transcribe("whisper-1", audio_content)
        user_text = transcription['text']
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Paso 2: Genera una respuesta con GPT-4 basado en el texto transcrito
    try:
        response = openai.Completion.create(
            engine="text-davinci-004",  # Asegúrate de usar el motor adecuado
            prompt=user_text,
            max_tokens=50
        )
        generated_text = response['choices'][0]['text']
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # (Opcional) Paso 3: Convierte el texto de respuesta en audio
    # Si tienes acceso a una API de Text-to-Speech, este es el lugar donde harías la conversión
    # y luego retornarías el audio en lugar de texto.

    return jsonify({"transcription": user_text, "response": generated_text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
