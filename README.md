# marvel-character-db
Marvel Character Database App
Marvel App Code Files*
We'll use Python and Flask framework. Create these files in your local project folder:

1.  app.py - main application file

2.  models.py - character data models

3.  repositories.py - database interactions

4.  requirements.txt - dependencies list

Here’s a sneak peek of app.py:
from flask import Flask, jsonify
app = Flask(__name__)
characters = [
    {"id": 1, "name": "Iron Man"},
    {"id": 2, "name": "Captain America"}
]
@app.route('/characters', methods=['GET'])
def get_characters():
    return jsonify(characters)
if __name__ == '__main__':
    app.run()
