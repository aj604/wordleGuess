import unittest
from Functionality.wordle import *

class TestClassFuncs(unittest.TestCase):
        
    def test_setWord(self):
        game = Wordle(False)
        game.setWord("aaaaa")
        self.assertEqual(game.target, "aaaaa")

    def test_guessHistory(self):
        game = Wordle(False)
        game.guessWord("aaaaa")
        self.assertEqual(game.guessHistory[0], "aaaaa")

    def test_gameWon(self):
        game = Wordle(False)
        game.setWord("aaaaa")
        game.guessWord("aaaaa")
        self.assertTrue(game.gameWon)
        
    def test_reset(self):
        game = Wordle(False)
        game.setWord("aaaaa")
        game.guessWord("abcde")
        game.reset()
        self.assertEqual(game.greenLetters, "_____")
        self.assertEqual(game.yellowLetters, "")
        self.assertEqual(game.badLetters, "")
        self.assertFalse(game.gameWon)
        self.assertEqual(game.guesses, 0)
        self.assertEqual(game.guessHistory, [])
        self.assertEqual(game.greenHistory, [])
        self.assertEqual(game.yellowHistory, [])
        self.assertEqual(game.badHistory, [])
