
from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Dummy knowledge base (replace with actual data source)
knowledge_base = {
    "booking": "You can book a table by providing your name, number of guests, and time.",
    "menu": "Our menu includes a variety of vegetarian and non-vegetarian dishes.",
    "cancellation": "To cancel a booking, simply reply with 'cancel' followed by your booking ID.",
}

# Function to manage token size (mock token size here for simplicity)
def split_into_chunks(text, max_tokens=800):
    words = text.split()
    num_chunks = math.ceil(len(words) / max_tokens)
    return [' '.join(words[i * max_tokens: (i + 1) * max_tokens]) for i in range(num_chunks)]

@app.route('/query', methods=['GET'])
def query_knowledge_base():
    user_query = request.args.get('query', '').lower()
    
    # Mock tokenized responses based on query
    if user_query in knowledge_base:
        response_text = knowledge_base[user_query]
        chunks = split_into_chunks(response_text)
        return jsonify({"response": chunks[0]})  # Returning the first chunk for now
    else:
        return jsonify({"response": "Sorry, I don't have an answer to that question."})

if __name__ == '__main__':
    app.run(debug=True)
