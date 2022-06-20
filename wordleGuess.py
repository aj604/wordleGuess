# Based on guess and target, return green, yellow, and grey letters
def wordleGuess(guess, target):
  ret = {"greenLetters": "",
         "yellowLetters": "",
         "badLetters": ""}
  for i in range(5):
    if guess[i] == target[i]:
      ret["greenLetters"] += guess[i]
    else:
      ret["greenLetters"] += "_"
  for letter in guess:
    if letter in target:
      ret["yellowLetters"] += letter
    else:
      ret["badLetters"] += letter
  return ret
