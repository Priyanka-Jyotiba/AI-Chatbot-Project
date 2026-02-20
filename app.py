from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from database import init_db, save_chat

app = Flask(__name__)

# Initialize database when app starts
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    
    bot_response = get_response(user_message)
    
    # Save chat into database
    save_chat(user_message, bot_response)
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
