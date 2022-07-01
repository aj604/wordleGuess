#region IMPORT
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)

from ctypes.wintypes import WORD
from random import randrange
from enum import Enum
from functools import singledispatchmethod
from Functionality.wordleGuess import wordleGuess
from Functionality.bestGuess import bestGuess
from StaticData.StaticData import POSSIBLE_GUESSES, WORD_LIST
import os
#endregion


#Enum for GameState
class GameState(Enum):
  Win = 1
  OutOfTurns = 2

#Wordle Game Handler
class Wordle:

  @singledispatchmethod
  def __init__(self, arg):
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
    
    self.showHints = False
  

  @__init__.register
  def _(self, id: int):
    self.target = WORD_LIST[id if id < len(WORD_LIST) and id > 0 else 0]
    
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
    
    self.showHints = False


  @__init__.register
  def _(self, target: str):
    self.target = target
    
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
    
    self.showHints = False


  @__init__.register
  def _(self, hintsFlag: bool):
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
    
    self.showHints = hintsFlag

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

  #Sets the current word for guess stats
  def setWord(self, word):
    self.reset()
    self.target = word

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

        
  # Helper Function to Print Results
  def printResults(self):
    print(f'Green Letters  : {self.greenHistory[self.guesses-1]}')
    print(f'Yellow Letters : {self.yellowHistory[self.guesses-1]}')
    print(f'Bad Letters    : {self.badLetters}{os.linesep}')
    print(f'Overall Green  : {self.greenLetters}{os.linesep}')
    
  #Handles prompting user for their guess, and calls the guess function
  def promptGuess(self):
    guess = input(f'Enter Guess #{self.guesses+1}: ')
    while guess not in POSSIBLE_GUESSES:
      print(f'Sorry, {guess} is not a valid word')
      guess = input(f'Enter Guess #{self.guesses+1}: ')
    print()

    self.guessWord(guess)
    print("Nice Guess!\n")
    self.printResults()
    if self.showHints:
      self.printHints()
    
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
