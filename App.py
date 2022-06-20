from wordle import Wordle
def App():
  game = Wordle()
  print("Welcome to NB Wordle!\n")
  while True:
    game.promptGuess()
    if(game.gameWon):
      print("Thanks for Playing\n")
      resp = input("Do you want to play again? (Y or N): ")
      if resp == "Y" or resp == "y":
        game.reset()
      else:
        print("Goodbye")
        break

App()
  