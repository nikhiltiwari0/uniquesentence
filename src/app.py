from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

FILENAME = "sentences.json"

def load_sentences():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_sentences(sentences):
    with open(FILENAME, "w") as f:
        json.dump(sentences, f)

# API Route to add or check a sentence
@app.route("/sentence", methods=["POST"])
def add_sentence():
    data = request.get_json()
    unique_input = data.get("sentence").lower()

    sentences = load_sentences()

    if unique_input in sentences:
        sentences[unique_input] += 1
        message = f"Not a unique sentence, this sentence has been submitted {sentences[unique_input]} times before!"
    else:
        sentences[unique_input] = 1
        message = "You found a unique sentence!" 

    save_sentences(sentences)

    return jsonify({"message": message, "sentences": sentences})

if __name__ == "__main__":
    app.run(debug=True)
