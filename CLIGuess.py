from bestGuess import bestGuess
# CLI Entry Point to use only the bestGuess function
def App():
  greenLetters = input('Please enter your green letters, while preseving the spacing with "_": ')
  yellowLetters = input("Please enter a combined string of all yellow letters: ")
  badLetters = input("Please enter any excluded letters: ")
  guesses = int(input("How many Guesses have you made so far?"))
  yellowLetterHistory = []
  for i in range(guesses):
    yellowHistory = input(f'Please enter the yellow numbers from guess #{i}, using "_" to preserve spaces: ')
    yellowLetterHistory.append(yellowHistory if yellowHistory != "" else "_____")
  res = bestGuess(greenLetters, yellowLetters, badLetters, yellowLetterHistory)
  print("Word Scores:")
  print("______________")
  for word in res:
    print(f'| {word} | {res[word]} |')
  print("______________\n")

App()