import json

FILENAME = "sentences.json"

# Load existing sentences
try:
    with open(FILENAME, "r") as f:
        sentences = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    sentences = {}  # Default dictionary

unique_input = input("Tell me a unique sentence: ")

if unique_input.lower() in sentences:
    print("Not a unique sentence/phrase, this sentence/phrase has been said", sentences[unique_input.lower()], "times!")
    sentences[unique_input.lower()] += 1
else:
    print("You found a unique sentence!")
    sentences[unique_input.lower()] = 1

# Save updated sentences
with open(FILENAME, "w") as f:
    json.dump(sentences, f)

print(sentences)
