from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Configura tu clave de API de OpenAI desde una variable de entorno
openai.api_key = os.environ.get("sk-proj-c3V6jLr8MltEyY3TdHfIT3BlbkFJqsrUf6TaKuwBrafWaFjS")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Puedes cambiar el modelo si lo deseas
        messages=[{"role": "user", "content": user_input}]
    )
    
    answer = response.choices[0].message.content.strip()
    return render_template('index.html', user_input=user_input, bot_response=answer)

if __name__ == '__main__':
    # Usar el puerto asignado por Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



