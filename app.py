from flask import Flask, jsonify
from marvel_data import characters

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Marvel API!"

@app.route('/characters')
def get_characters():
    return jsonify(characters)

@app.route('/characters/<name>')
def get_character(name):
    char = next((c for c in characters if c['name'].lower() == name.lower()), None)
    return jsonify(char if char else {"error": "Character not found"}), 200 if char else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


