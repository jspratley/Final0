__author__ = 'Noel'

import unittest
from lang_proc import nltktest


class LanguageProcessingTest(unittest.TestCase):

    def test_single_sentence(self):
        """
        Tests whether a single sentence achieves the expected output.
        """
        test_sentence = "Hello here is sentence."

        expected_lexicon = {'NOUN': ['hello', 'sentence'], 'ADV': ['here'], '.': ['.'], 'VERB': ['is']}
        lexicon = {}
        nltktest.add_sentence(test_sentence, lexicon)

        self.assertEqual(expected_lexicon, lexicon)

    def test_single_sentence_no_punctuation_easy(self):
        """
        Tests whether a single sentence achieves the expected output while stripping away punctuation.
        """
        test_sentence = "Hello here is sentence."

        expected_lexicon = {'NOUN': ['hello', 'sentence'], 'ADV': ['here'], 'VERB': ['is']}
        lexicon = {}
        nltktest.add_paragraph_no_punctuation(test_sentence, lexicon)

        self.assertEqual(expected_lexicon, lexicon)

    def test_single_sentence_no_punctuation_harder(self):
        """
        Tests whether a single sentence achieves the expected output while stripping away punctuation.
        """
        test_sentence = "Hello?!! here is.?!?! sentence.?!?!!!"

        expected_lexicon = {'NOUN': ['hello', 'sentence'], 'ADV': ['here'], 'VERB': ['is']}
        lexicon = {}

        nltktest.add_paragraph_no_punctuation(test_sentence, lexicon)

        self.assertEqual(expected_lexicon, lexicon)

    def test_add_multiple_sentences(self):
        """
        Tests whether multiple sentences can be properly added to a lexicon with punctuation.
        """
        test_sentence = "Hello! Welcome to my paragraph. This is the greatest literary work of our generation. Your eyes cannot handle the debonair stylings of my sumptuous, florid, and resplendent locution!"

        expected_lexicon = {'PRT': ['to'], '.': ['!', '.', ','], 'ADP': ['of'], 'DET': ['this', 'the'], 'VERB': ['is', 'can', 'handle'], 'CONJ': ['and'], 'PRON': ['my', 'our', 'your'], 'X': ['welcome'], 'ADV': ['not'], 'NOUN': ['hello', 'paragraph', 'work', 'generation', 'eyes', 'debonair', 'stylings', 'locution'], 'ADJ': ['greatest', 'literary', 'sumptuous', 'florid', 'resplendent']}
        lexicon = {}

        nltktest.add_paragraph(test_sentence, lexicon)

        self.assertEqual(expected_lexicon, lexicon)

    def test_add_multiple_sentences_no_punctuation(self):
        """
        Tests whether multiple sentences can be properly added to a lexicon with no punctuation.
        """
        test_sentence = "Hello! Welcome to my paragraph. This is the greatest literary work of our generation. Your eyes cannot handle the debonair stylings of my sumptuous, florid, and resplendent locution!"

        expected_lexicon ={'PRON': ['my', 'our', 'your'], 'PRT': ['to'], 'DET': ['this', 'the'], 'ADJ': ['greatest', 'literary', 'sumptuous', 'florid', 'resplendent'], 'NOUN': ['hello', 'welcome', 'paragraph', 'work', 'generation', 'eyes', 'debonair', 'stylings', 'locution'], 'VERB': ['is', 'cannot', 'handle'], 'CONJ': ['and'], 'ADP': ['of']}
        lexicon = {}

        nltktest.add_paragraph_no_punctuation(test_sentence, lexicon)

        self.assertEqual(expected_lexicon, lexicon)

    def test_add_sentence_complex(self):
        """
        Tests whether complex tagging (i.e. not Universal tagset) works properly.
        """
        test_sentence = "Your eyes cannot handle the debonair stylings of my sumptuous, florid, and resplendent locution"

        expected_lexicon = {'DT': ['the'], 'NNS': ['eyes', 'stylings'], 'IN': ['of'], 'RB': ['not'], 'CC': ['and'], ',': [','], 'MD': ['can'], 'JJ': ['sumptuous', 'florid', 'resplendent'], 'VB': ['handle'], 'PRP$': ['your', 'my'], 'NN': ['debonair', 'locution']}
        lexicon = {}

        nltktest.add_sentence_complex(test_sentence, lexicon)

        self.assertEqual(expected_lexicon, lexicon)