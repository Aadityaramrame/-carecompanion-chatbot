from flask import Flask, request, jsonify
from chatbot_functions import get_chatbot_response  # update if your function/class is different

app = Flask(__name__)

@app.route('/')
def home():
    return "CareCompanion Chatbot API is running."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("text", "")
    
    if not user_input:
        return jsonify({"error": "Missing 'text' in request"}), 400

    try:
        response = get_chatbot_response(user_input)  # Call your chatbot logic
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
