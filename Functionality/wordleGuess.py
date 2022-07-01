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
  for i in range(5):
    if guess[i] in target:
      ret["badLetters"] += "_"
      if guess[i] == target[i]:
        ret["yellowLetters"] += "_"
      else:
        ret["yellowLetters"] += guess[i]
    else:
      ret["badLetters"] += guess[i]
      ret["yellowLetters"] += "_"
  return ret

