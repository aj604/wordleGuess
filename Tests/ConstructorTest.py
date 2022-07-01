#region IMPORT
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)

import unittest
from Functionality.wordle import *
#endregion

class TestConstructors(unittest.TestCase):

    def test_string(self):       
        self.assertEqual(Wordle("Tests").target, "Tests")
    
    def test_id(self):
        self.assertEqual(Wordle(0).target, "added")

    def test_bool(self):
        self.assertTrue(Wordle(True).showHints)

    def test_any(self):
        self.assertFalse(Wordle(1.1).showHints)

    def test_OutOfRangeID(self):
        self.assertEqual(Wordle(999).target, "added")
