from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simulated knowledge base
responses = {
    "hello": [
        "Hello there! 😊 How can I assist you today?",
        "Hey! 👋 Nice to see you. What can I do for you?",
        "Hi! I'm here to help. Ask me anything!"
        ],

    "bye": [
        "Goodbye! 👋 Take care!",
        "See you later! Have a great day! 😊",
        "Farewell! Feel free to come back anytime!"
    ],
    "your name": [
        "I'm PyBot 🤖, your virtual assistant!",
        "They call me PyBot! 🧠 How can I help?",
        "Name’s PyBot – your chatbot companion!"
    ],
    "default": [
        "I'm still learning... 🤔 Could you rephrase that?",
        "Interesting question! Let me think... 💭",
        "Hmm, I’m not sure how to respond to that yet. Try something else?"
    ],
    "salam": [
        "wsalam",




    ],
    "how are you?": [
        "I am good what about you",

    ],
}

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    for keyword, possible_responses in responses.items():
        if keyword in user_message:
            return jsonify({"response": random.choice(possible_responses)})

    return jsonify({"response": random.choice(responses["default"])})

if __name__ == "__main__":
    app.run(debug=True)
