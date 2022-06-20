from wordle import Wordle, GameState

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