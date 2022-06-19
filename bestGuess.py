from collections import Counter

# Scoring Function
# Takes in a list of dictionarys with corresponding scores by letter position
def wordScore (word, freq) -> int:
    score = 0
    for letter in set(word):
      letterOccurances = positionsOfChar(letter, word)
      letterScores = maxLetterScoreRanked(letter, freq)
      for letterIndex in letterScores.keys():
        if letterIndex in letterOccurances:
          score += letterScores[letterIndex]
          break
    return score

# Given a word and a Character, returns a list of its indexes
def positionsOfChar(c, word):
  ret = []
  for i in range(len(word)):
    if(word[i] == c): 
      ret.append(i)
  return ret
  
# Letter Scoring Function
# Returns a list of dictionarys with letter scores by poition
def letterScore(wordList):
  scores = []
  for i in range(5):
    scores.append(nthLetterOfWords(i, wordList))
  return scores

# Returns dict of index : score, sorted in desc order by score
def maxLetterScoreRanked(letter, freq):
  res = {}
  for i in range(5):
    if letter in freq[i]:
      res[i]= freq[i][letter]
  return dict(sorted(res.items(),key=lambda item:item[1], reverse=True))
  
  
# Pre: Letters with required position, required letters, and excluded letters
# Post: Possible words
# Dont forget the case where position letters can occur multiple times
def possibleWords(positionLetters, requiredLetters, excludedLetters, wordList):

  # Position Letter Loop
  for i in range(5):
    if positionLetters[i] != ' ':
      wordList = wordsWithLetterInPosition(positionLetters[i], i, wordList)

  # Required Letter Loop
  for letter in requiredLetters:
    wordList = wordsWithLetter(letter, wordList)

  # Excluded Letter Loop
  for letter in excludedLetters:
    wordList = wordsWithoutLetter(letter, wordList)
  
  return wordList
# Given a letter and a wordList, return a new wordList
# containing only words that dont have the given letter
def wordsWithoutLetter(letter, wordList):
  ret = []
  for word in wordList:
    if letter not in word:
      ret.append(word)
  return ret
  

  
# Given a letter and a wordList, return a new wordList 
# containing only words with that letter
def wordsWithLetter(letter, wordList):
  ret = []
  for word in wordList:
    if letter in word:
      ret.append(word)
  return ret

  
#Given a letter and aposition, returns a new wordlist that satisifies
def wordsWithLetterInPosition(letter, position, wordList):
  ret = []
  for word in wordList:
    if word[position] == letter:
      ret.append(word)
  return ret
  

#Frequency of letters based on position
def nthLetterOfWords(n, wordList):
  letters = ""
  for word in wordList:
    letters += word[n]
  return Counter(letters)
  



# Main Function
# Takes in letters within the word, and letters not in the word
# Outputs possible words remaining, and scores them based on letter frequency
def bestGuess(positionLetters, requiredLetters, excludedLetters):
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
    if len(positionLetters) != 5:
      if positionLetters == "":
        positionLetters = "     "
      else:
        while len(positionLetters) < 5:
          positionLetters += " "

    # Reduce wordList to only words that give correct solution
    wordList = possibleWords(positionLetters, requiredLetters, excludedLetters, wordList)

    # Generate Scores based on reduced word list
    scores = letterScore(wordList)

    res = {}
    for i in wordList:
      res[i] = wordScore(i,scores)

    # Sort results by descending scores
    res = dict(sorted(res.items(),key=lambda item:item[1], reverse=True))
  
    return res




#postition = "     "
#goodLetters = ""
#badLetters = ""

#bestGuess("     ", "rts", "ae")
#print(wordScore("sssss", letterScore(wordList)))
#print(letterScore(wordList))

