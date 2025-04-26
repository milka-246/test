from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Привет! Я простой чат-бот. Отправь мне POST-запрос с JSON {'message': 'текст'}, и я отвечу!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    if "привет" in user_message:
        response = "Привет! Как дела?"
    elif "как дела" in user_message:
        response = "Отлично! А у тебя?"
    elif "пока" in user_message:
        response = "До встречи! Было приятно пообщаться."
    else:
        response = "Я пока не понимаю. Попробуй сказать 'привет', 'как дела' или 'пока'."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
