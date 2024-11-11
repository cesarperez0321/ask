from flask import Flask, request, jsonify
from flask_cors import CORS  # Asegúrate de importar esto

import openai

openai.api_key = "sk-proj-c3V6jLr8MltEyY3TdHfIT3BlbkFJqsrUf6TaKuwBrafWaFjS"  # Coloca tu clave de API aquí

app = Flask(__name__)
CORS(app)  # Esto aplica CORS globalmente

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get("question")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    try:
        response = openai.Completion.create(
            engine="gpt-4",  # O usa "gpt-4" si tienes acceso
            prompt=user_question,
            max_tokens=150
        )
        answer = response['choices'][0]['text'].strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Cambié esto para asegurarte de que Flask escuche en todos los puertos
