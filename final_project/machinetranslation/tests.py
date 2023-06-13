""" Module Docstring: Translation Tests """
import unittest
from . import translator

class TranslationTests(unittest.TestCase):
    """ Class Docstring: translation test class """
    def test_hello(self):
        """ Test Hello translates to Bonjour"""
        test = translator.englishToFrench('Hello')
        self.assertEqual(test, 'Bonjour')

    def test_bonjour(self):
        """ Test Bonjour translates to Hello"""
        test = translator.frenchToEnglish('Bonjour')
        self.assertEqual(test,'Hello')


if __name__ == '__main__':
    unittest.main()
