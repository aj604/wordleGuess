import json
from flask import Flask, request, jsonify
from bestGuess import bestGuess

app = Flask(__name__)
@app.route('/', methods=['POST'])
def wordleGuess():
  data = json.loads(request.data)
  greenLetters = data['greenLetters']
  yellowLetters = data['yellowLetters']
  badLetters = data['badLetters']
  return json.dumps(bestGuess(greenLetters, yellowLetters, badLetters), indent=4)
app.run()
