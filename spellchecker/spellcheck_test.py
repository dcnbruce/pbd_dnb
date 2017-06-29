# spellcheck_test.py
import unittest
from spellchecker import spellChecker

class TestspellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = spellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_Checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        self.assertFalse(self.spellChecker.check_words('zygotic mistasdas elementary'))
        self.assertTrue(self.spellChecker.check_words('our first correct sentence'))
		# handle case sensitivity
        self.assertTrue(self.spellChecker.check_words('Our first correct sentence'))
        # handle full stop
        self.assertTrue(self.spellChecker.check_words('Our first correct sentence.'))

if __name__ == '__main__':
    unittest.main()
