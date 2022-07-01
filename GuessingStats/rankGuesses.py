from Functionality.wordle import *
from StaticData import WORD_LIST


def rankGuesses():
    game = Wordle()
    scores = {}

    #Loop through possible targets
    for targetWord in WORD_LIST: 
        game.setWord(targetWord)

        #Loop through possible first Guesses
        for firstGuess in WORD_LIST: #Update Later to 