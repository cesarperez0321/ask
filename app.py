import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Tu clave API de OpenAI
openai.api_key = "sk-proj-c3V6jLr8MltEyY3TdHfIT3BlbkFJqsrUf6TaKuwBrafWaFjS"  # Reemplaza con tu clave de API real

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get("question")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Haciendo la llamada correcta para openai>=1.0.0
        response = openai.Completion.create(
            model="gpt-4",  # O "gpt-4" si tienes acceso
            prompt=user_question,
            max_tokens=150
        )

        # Extraer la respuesta
        answer = response['choices'][0]['text'].strip()

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
