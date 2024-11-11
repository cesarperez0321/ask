import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Configura tu clave de API de OpenAI
openai.api_key = "sk-proj-c3V6jLr8MltEyY3TdHfIT3BlbkFJqsrUf6TaKuwBrafWaFjS"  # Reemplaza esto con tu clave API real

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get("question")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Usando la nueva API de OpenAI con ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Puedes usar "gpt-4" si tienes acceso
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ]
        )
        
        # Extraer la respuesta generada
        answer = response['choices'][0]['message']['content'].strip()
        
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
