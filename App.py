from wordle import Wordle
def App():
  print("Welcome to NB Wordle!\n")
  hintsChoice = input("Do you want hints? ;) ")
  hintsFlag = True if hintsChoice.lower() == "y" else False 
  game = Wordle(hintsFlag)

  while True:
    game.promptGuess()
    if(game.gameWon):
      print("Thanks for Playing\n")
      resp = input("Do you want to play again? (Y or N): ")
      if resp.lower() == "y":
        game.reset()
      else:
        print("Goodbye")
        break

App()
  