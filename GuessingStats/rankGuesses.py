#region IMPORT
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)

from itertools import islice
from datetime import datetime

from Functionality.wordle import *
from Functionality.bestGuess import *
from StaticData.StaticData import WORD_LIST, POSSIBLE_GUESSES
#endregion


def rankGuesses():
    game = Wordle(False)
    scores = {}
    nextGuess = ""
    targetLen = len(POSSIBLE_GUESSES)
    possibleLen = len(POSSIBLE_GUESSES)
    funcStart = datetime.now()
    wordsGuessed = 0
    gamesPlayed = 0
    maxGuess = 0

    
    #Loop through possible first Guesses
    for firstGuess in POSSIBLE_GUESSES: #Update Later to use possible guesses instead of target list
        #initialize word score to 0
        scores[firstGuess] = 0
        wordsGuessed += 1
        #if wordsGuessed % 5 == 0:
        print(f'Processing... {possibleLen - wordsGuessed} words remain. Elapsed Time: {(datetime.now() - funcStart).total_seconds()}s')
    
        #Loop through possible targets
        for targetWord in POSSIBLE_GUESSES: 
            currentWordList = POSSIBLE_GUESSES
            gameStart = datetime.now()
            game.setWord(targetWord)
            game.guessWord(firstGuess)
            
            #Loop through best guesses until game is won
            while not game.gameWon:
                if game.guesses == 6:
                    game.guesses += 5
                    break
                [nextGuess, currentWordList] = bestSingleGuessWordList(game.greenLetters, game.yellowLetters, game.badLetters, game.yellowHistory, currentWordList)
                #nextGuess = next(iter(bestGuesses))
                game.guessWord(nextGuess)
            
            #Add guesses required to get to target to score. Normalize later based on target len
            scores[firstGuess] += game.guesses
            gamesPlayed += 1
            if gamesPlayed % 5000 == 0:
                print(f'{gamesPlayed} games played. Total Time: {(datetime.now() - funcStart)}')

    #Normalize scores to average guesses to target            
    avgGuess = 0.0
    #bestWord = 0.0
    for guess in scores:
        scores[guess] /= targetLen
        avgGuess += scores[guess]
    
    scores = dict(sorted(scores.items(),key=lambda item:item[1]))

    avgGuess /= possibleLen
    

    print(f'Average Guesses to Target: {round(avgGuess, 2)}')
    print("______________")
    for word in islice(scores, 150):
      print(f'| {word} | {scores[word]:.2f} |')
    print("______________\n")

    funcTime = datetime.now() - funcStart
    print(f'Function took {funcTime.total_seconds()}s')

rankGuesses()
