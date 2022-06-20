from bestGuess import *

WORD_LIST = {"added", 
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
            "yield"}

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

  
print(wordleGuess("aaaye", "abcde"))
print(bestGuess("_a___", "", ""))