from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Configura CORS para permitir solicitudes desde tu dominio de Firebase
CORS(app, resources={r"/*": {"origins": "*"}})

# Configura tu clave de API de OpenAI desde una variable de entorno
openai.api_key = os.environ.get("sk-proj-c3V6jLr8MltEyY3TdHfIT3BlbkFJqsrUf6TaKuwBrafWaFjS")

@app.route('/get_response', methods=['POST', 'OPTIONS'])
@cross_origin()
def get_response():
    if request.method == 'OPTIONS':
        # Responder a la solicitud preflight
        response = app.make_default_options_response()
        return response

    data = request.get_json()
    user_input = data.get('user_input', '')

    try:
        # Llamada a la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({'bot_response': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Usar el puerto asignado por Render
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

