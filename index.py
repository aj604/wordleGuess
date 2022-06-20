from flask import Flask, render_template
from wordle import Wordle

app = Flask(__name__)

@app.route('/')
def index():
  game = Wordle(False)
  game.guessWord("rates")
  
  game.guessWord("rates")
  
  game.guessWord("rates")
  
  game.guessWord("rates")
  
  game.guessWord("rates")
  
  game.guessWord("rates")
  return render_template('index.html', game = game)

app.run()