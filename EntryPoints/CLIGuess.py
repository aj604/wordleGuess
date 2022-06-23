from Functionality.bestGuess import bestGuess
# CLI Entry Point to use only the bestGuess function
def App():
  isSolved = False
  yellowLetterHistory = []
  yellowLetters = ""
  yellowHistory = ""
  guesses = int(input("How many Guesses have you made so far? "))
  if guesses == 0:
    print("Please make your first guess. \n_Here are some hints.")
    printScores(bestGuess("","","",""))
  for i in range(guesses):
    yellowHistory = input(f'Please enter the yellow numbers from guess #{i}, using "_" to preserve spaces: ')
    for letter in yellowHistory:
      if letter != "_": yellowLetters += letter
    yellowLetterHistory.append(yellowHistory if yellowHistory != "" else "_____")
  while not isSolved:
    [greenLetters, yellowLetters, badLetters] = getInput()
    yellowLetterHistory.append(yellowLetters)
    for letter in yellowHistory:
      if letter != "_": yellowLetters += letter
    res = bestGuess(greenLetters, yellowLetters, badLetters, yellowLetterHistory)
    printScores(res)
    isSolved = True if input("Did you solve it? (Y) ")[0].lower() == "y" else False
  print("Good Job!")

def getInput():
  greenLetters = input('Please enter your green letters, while preseving the spacing with "_": ')
  yellowLetters = input(f'Please enter the yellow numbers, using "_" to preserve spaces: ')
  badLetters = input("Please enter any excluded letters: ")
  return [greenLetters, yellowLetters, badLetters]

def printScores(res):
    print("Word Scores:")
    print("______________")
    for word in res:
      print(f'| {word} | {res[word]} |')
    print("______________\n")

App()