from collections import Counter

# Scoring Function
# Takes in a list of dictionarys with corresponding scores by letter position
# TODO: Count only the max letter score per letter
def wordScore (word, freq) -> int:
    score = 0
    for letter in word:
      for i in range(0,4):
        score += freq[i][letter]
    return score

# Letter Scoring Function
# Returns a list of dictionarys with letter scores by poition
def letterScore(wordList):
  scores = []
  for i in range(1,5):
    scores.append(nthLetterOfWords(i, wordList))
  return scores

#TODO
def possibleWords(wordList):
  return wordList

# 1 based
  
#Frequency of letters based on position
def nthLetterOfWords(n, wordList):
  letters = ""
  for word in wordList:
    letters += word[n-1]
  return Counter(letters)
  



# Main Function
# Takes in letters within the word, and letters not in the word
# Outputs possible words remaining, and scores them based on letter frequency
def bestGuess(goodLetters, badLetters):
    wordList = {"added", 
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

    store = letterScore(wordList)

    badLettersArray = list(badLetters)
    goodLettersArray = list(goodLetters)

    badFlag = 0

    res = {}

    for i in wordList:
        badFlag = 0
        while badFlag == 0:
            for goodLetter in goodLettersArray:
                if goodLetter not in i:
                    badFlag = 1
            for badLetter in badLettersArray:
                if badLetter in i:
                    badFlag = 1
            if badFlag == 0:
                badFlag = 1
                res[i] = wordScore(i,store)
    res = dict(sorted(res.items(),key=lambda item:item[1], reverse=True))
    for key in res:
        print(f'{key} - Score: {res[key]}')
bestGuess("","")
wordList = {"added", 
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

#print(letterScore(wordList))