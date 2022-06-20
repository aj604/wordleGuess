from random import randrange
from wordleGuess import wordleGuess
from bestGuess import bestGuess
import os

WORD_LIST = ["added", 
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
            "yield"]

class Wordle:
  def __init__(self, showHints):
    self.target = WORD_LIST[randrange(len(WORD_LIST))]
    self.greenLetters = "_____"
    self.yellowLetters = ""
    self.badLetters = ""
    self.gameWon = False
    self.guesses = 0
    self.showHints = showHints

  def guessWord(self, word):
    self.guesses += 1
    if word == self.target:
      self.gameWon = True
      print(f'You Won! {word} was the target word!{os.linesep}It took you {self.guesses} guesses!')
    else:
      res = wordleGuess(word, self.target)
      greenLetterList = list(self.greenLetters)
      for i in range(5): 
        if res["greenLetters"][i] != "_":
          greenLetterList[i] = res["greenLetters"][i]
      self.greenLetters = "".join(greenLetterList)
      for letter in res["yellowLetters"]:
        if letter not in self.yellowLetters:
          self.yellowLetters += letter
      for letter in res["badLetters"]:
        if letter not in self.badLetters:
            self.badLetters += letter
      print(f'Nice Guess!{os.linesep}Green Letters : {self.greenLetters}{os.linesep}Yellow Letters   : {self.yellowLetters}{os.linesep}Bad Letters   : {self.badLetters}{os.linesep}')
      if self.showHints:
        print(bestGuess(self.greenLetters, self.yellowLetters, self.badLetters))

  def promptGuess(self):
    guess = input("Enter Your Guess: ")
    self.guessWord(guess)

  def reset(self):
    self.guesses = 0
    self.gameWon = False
    self.target = WORD_LIST[randrange(len(WORD_LIST))]
    self.greenLetters = "_____"
    self.yellowLetters = ""
    self.badLetters = ""