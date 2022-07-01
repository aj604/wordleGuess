#region IMPORT
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)


from Functionality.wordle import *
from Functionality.bestGuess import *
from StaticData.StaticData import WORD_LIST
#endregion


def rankGuesses():
    game = Wordle(False)
    scores = {}
    nextGuess = ""
    targetLen = len(WORD_LIST)

    
    #Loop through possible first Guesses
    for firstGuess in WORD_LIST: #Update Later to use possible guesses instead of target list
        #initialize word score to 0
        scores[firstGuess] = 0
    
        #Loop through possible targets
        for targetWord in WORD_LIST: 
            
            game.setWord(targetWord)
            game.guessWord(firstGuess)
            
            #Loop through best guesses until game is won
            while not game.gameWon:
                bestGuesses = bestGuess(game.greenLetters, game.yellowLetters, game.badLetters, game.yellowHistory)
                nextGuess = next(iter(bestGuesses))
                game.guessWord(nextGuess)
            
            #Add guesses required to get to target to score. Normalize later based on target len
            scores[firstGuess] += game.guesses

    #Normalize scores to average guesses to target            
    avgGuess = 0.0
    #bestWord = 0.0
    for guess in scores:
        scores[guess] /= targetLen
        avgGuess += scores[guess]
    
    scores = dict(sorted(scores.items(),key=lambda item:item[1]))

    avgGuess /= targetLen
    print(f'Average Guesses to Target: {round(avgGuess, 2)}')
    print("______________")
    for word in scores:
      print(f'| {word} | {scores[word]:.2f} |')
    print("______________\n")

rankGuesses()