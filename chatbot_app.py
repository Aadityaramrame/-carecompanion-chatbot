from flask import Flask, request, jsonify
from chatbot_functions import DataProcessor, Chatbot  # Correct import

app = Flask(__name__)

# Initialize chatbot once
data_processor = DataProcessor()
chatbot = Chatbot(data_processor)

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
        matched_question, response, source = chatbot.get_response(user_input)
        return jsonify({
            "matched_question": matched_question,
            "response": response,
            "source": source
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
