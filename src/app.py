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

@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    num_displayed = request.args.get("limit", default=5, type=int)  # Default to top 5

    sentences = load_sentences()

    sorted_sentences = sorted(sentences.items(), key=lambda item: item[1], reverse=True)

    leaderboard = sorted_sentences[:num_displayed]

    return jsonify({"leaderboard": leaderboard})

# API Route to add or check a sentence
@app.route("/sentence", methods=["POST"])
def add_sentence():
    data = request.get_json()
    unique_input = data.get("sentence").lower()

    sentences = load_sentences()

    if unique_input in sentences:
        sentences[unique_input] += 1
        message = f"Not a unique sentence, this sentence has been submitted {sentences[unique_input]-1} times before!"
    else:
        sentences[unique_input] = 1
        message = "You found a unique sentence!" 

    save_sentences(sentences)

    return jsonify({"message": message, "sentences": sentences})

if __name__ == "__main__":
    from waitress import serve
    app.run(debug=True)
