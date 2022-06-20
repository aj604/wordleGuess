from random import randrange
from wordleGuess import wordleGuess

WORD_LIST = {"added", 
            "agent", 
            "alpha", 
            "asset", 
            "audit", 
            "basis", 
            "board", 
            "bonus", 
            "brand", 
            "check", 
            "close", 
            "count", 
            "cover", 
            "curve", 
            "cycle", 
            "debit", 
            "delta", 
            "draft", 
            "entry", 
            "equal", 
            "error", 
            "files", 
            "first", 
            "flows", 
            "funds", 
            "gross", 
            "hedge", 
            "index", 
            "issue", 
            "labor", 
            "limit", 
            "loans", 
            "model", 
            "money", 
            "offer", 
            "order", 
            "point", 
            "price", 
            "rates", 
            "ratio", 
            "risks", 
            "right", 
            "round", 
            "sales", 
            "scale", 
            "scope", 
            "share", 
            "sheet", 
            "shock", 
            "stock", 
            "swaps", 
            "taxes", 
            "terms", 
            "trade", 
            "trust", 
            "value", 
            "vests", 
            "yield"}

class Wordle:
  def __init__(self):
    self.target = WORD_LIST[randrange(len(WORD_LIST))]
    self.greenLetters = ""
    self.yellowLetters = ""
    self.badLetters = ""
    self.gameWon = False
    self.guesses = 0

  def guessWord(self, word):
    self.guesses += 1
    if word == self.target:
      self.gameWon = True
      print(f'You Won! {word} was the target word! 
            It took you {self.guesses} guesses!')
    else:
      res = wordleGuess(word, self.target)
      self.greenLetters = res["greenLetters"]
      self.yellowLetters = res["yellowLetters"]
      self.badLetters = res["badLetters"]
      print(f'Nice Guess!
            Green Letters : {self.greenLetters}
            Red Letters   : {self.redLetters}
            Bad Letters   : {self.badLetters}
            ')

  def promptGuess():
    guess = input("Enter Your Guess:")
    guessWord(guess)
    