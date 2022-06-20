from random import randrange
from enum import Enum
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

#Enum for GameState
class GameState(Enum):
  Win = 1
  OutOfTurns = 2

#Wordle Game Handler
class Wordle:
  def __init__(self, showHints):
    self.target = WORD_LIST[randrange(len(WORD_LIST))]
    
    self.greenLetters = "_____"
    self.yellowLetters = ""
    self.badLetters = ""
    
    self.gameWon = False
    self.guesses = 0
    self.streak = 0
    
    self.guessHistory = []
    self.greenHistory = []
    self.yellowHistory = []
    self.badHistory = []
    
    self.showHints = showHints

  #Function to reset game, and start over
  def reset(self):
    self.target = WORD_LIST[randrange(len(WORD_LIST))]
    self.greenLetters = "_____"
    self.yellowLetters = ""
    self.badLetters = ""
    self.gameWon = False
    self.guesses = 0
    self.streak += 1
    self.guessHistory = []
    self.greenHistory = []
    self.yellowHistory = []
    self.badHistory = []
    
  #Internal Word Guessing Function
  def guessWord(self, word):
    self.guessHistory.append(word)
    self.guesses += 1
    
    if word == self.target:
      self.gameWon = True
      return
    
    else:
      res = wordleGuess(word, self.target)
      
      # Track Color History
      self.greenHistory.append(res["greenLetters"])
      self.yellowHistory.append(res["yellowLetters"])
      self.badHistory.append(res["badLetters"])

      greenLetterList = list(self.greenLetters)
      for i in range(5): 
        if res["greenLetters"][i] != "_":
          greenLetterList[i] = res["greenLetters"][i]
      self.greenLetters = "".join(greenLetterList)

      for letter in res["yellowLetters"]:
        if letter not in self.yellowLetters and letter != "_":
          self.yellowLetters += letter
      
      for letter in res["badLetters"]:
        if letter not in self.badLetters and letter != "_":
            self.badLetters += letter

      print("Nice Guess!\n")
      self.printResults()
      if self.showHints:
        self.printHints()
        
  # Helper Function to Print Results
  def printResults(self):
    print(f'Green Letters  : {self.greenHistory[self.guesses-1]}')
    print(f'Yellow Letters : {self.yellowHistory[self.guesses-1]}')
    print(f'Bad Letters    : {self.badLetters}{os.linesep}')
    print(f'Overall Green  : {self.greenLetters}{os.linesep}')
    
  #Handles prompting user for their guess, and calls the guess function
  def promptGuess(self):
    guess = input(f'Enter Guess #{self.guesses+1}: ')
    print()
    while len(guess) != 5:
      print("oops! your guess has to be 5 letters long!")
      guess = input(f'Enter Guess #{self.guesses+1}: ')
    self.guessWord(guess)
    
  #Handles End of Game Procedures
  def endGame(self, gameState):
    if gameState == GameState.Win:
      print(f'Congrats! You Won! {self.target} was the target word!{os.linesep}It took you {self.guesses} guesses!')
    if gameState == GameState.OutOfTurns:
      print("You ran out of guesses, Maybe next time...")
        
    resp = input("Do you want to play again? (Y or N): ")
    if resp.lower() == "y":
      self.reset()
      return False
    else:
      print("Goodbye")
      return True
      
  #Formatted print for Hints
  def printHints(self):
    hints = bestGuess(self.greenLetters, 
                          self.yellowLetters, 
                          self.badLetters,
                          self.yellowHistory)
    print("Word Scores:")
    print("______________")
    for word in hints:
      print(f'| {word} | {hints[word]} |')
    print("______________\n")
