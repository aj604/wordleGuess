import json
from flask import Flask, request
from bestGuess import bestGuess

app = Flask(__name__)
@app.route('/', methods=['POST'])
def wordleGuess():
  data = json.loads(request.data)
  return json.dumps(bestGuess(data['greenLetters'], 
                              data['yellowLetters'], 
                              data['badLetters']), 
                    indent=4)
app.run()
