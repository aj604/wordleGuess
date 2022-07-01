#region IMPORT
from ctypes.wintypes import WORD
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)

from collections import Counter
from StaticData.StaticData import POSSIBLE_GUESSES, WORD_LIST
#endregion


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
def possibleWords(positionLetters, requiredLetters, excludedLetters, yellowHistory, wordList):

  # Position Letter Loop
  for i in range(5):
    if positionLetters[i] != '_':
      wordList = wordsWithLetterInPosition(positionLetters[i], i, wordList)
 
  # Required Letter Loop
  for letter in requiredLetters:
    wordList = wordsWithLetter(letter, wordList)

 # Excluded Letter Loop
  for letter in excludedLetters:
    wordList = wordsWithoutLetter(letter, wordList)

  # Letter Not in Position Loop
  for yellowWord in yellowHistory:
    for i in range(5):
      if yellowWord[i] != "_":
        wordList = wordsWithoutLetterInPosition(yellowWord[i], i, wordList)
  return wordList


# Given a letter and a wordList, return a new wordList
# containing only words that dont have the given letter
def wordsWithoutLetter(letter, wordList):
  ret = []
  for word in wordList:
    if letter not in word:
      ret.append(word)
  return ret

  
# Given a letter, a position and a wordlist, return a new wordlist
# in which no words have that letter in that position
def wordsWithoutLetterInPosition(letter, position, wordList):
  ret = []
  for word in wordList:
    if word[position] != letter:
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


def normalizeLetters(word):
  if len(word) != 5:
    if word == "":
      word = "_____"
    else:
      while len(word) < 5:
        word += "_"
  return word




# Main Function
# Takes in letters within the word, and letters not in the word
# Outputs possible words remaining, and scores them based on letter frequency
def bestGuess(positionLetters, requiredLetters, excludedLetters, yellowHistory):

    normalizeLetters(positionLetters)

    # Reduce wordList to only words that give correct solution
    wordList = possibleWords(positionLetters, requiredLetters, excludedLetters, yellowHistory, WORD_LIST)

    # Generate Scores based on reduced word list
    scores = letterScore(wordList)

    res = {}
    for i in wordList:
      res[i] = wordScore(i,scores)

    # Sort results by descending scores
    res = dict(sorted(res.items(),key=lambda item:item[1], reverse=True))
  
    return res


def bestSingleGuess(positionLetters, requiredLetters, excludedLetters, yellowHistory):
  maxWord = ""
  maxScore = 0
  wordList = possibleWords(positionLetters, requiredLetters, excludedLetters, yellowHistory, POSSIBLE_GUESSES)
  scores = letterScore(wordList)

  for i in wordList:
    score = wordScore(i, scores)
    if score > maxScore:
      maxScore = score
      maxWord = i
  return { maxWord: maxScore }

def bestSingleGuessWordList(positionLetters, requiredLetters, excludedLetters, yellowHistory, wordList):
  maxScore = 0
  wordList = possibleWords(positionLetters, requiredLetters, excludedLetters, yellowHistory, wordList)
  scores = letterScore(wordList)

  for i in wordList:
    score = wordScore(i, scores)
    if score > maxScore:
      maxScore = score
      maxWord = i
  return [maxWord, wordList]
      



