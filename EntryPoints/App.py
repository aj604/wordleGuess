#region IMPORTS
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)
from Functionality.wordle import Wordle, GameState
#endregion

#CLI Entry Point
def App():
  print("Welcome to NB Wordle!\n")
  hintsChoice = input("Do you want hints? ;) ")
  hintsFlag = True if hintsChoice.lower() == "y" else False 
  game = Wordle(hintsFlag)

  while True:
    game.promptGuess()
    if game.gameWon and game.endGame(GameState.Win):
      break
    if game.guesses >= 6 and game.endGame(GameState.OutOfTurns):
      break

App()