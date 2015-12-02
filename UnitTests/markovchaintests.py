__author__ = 'Noel'

import unittest
from lang_proc import nltktest
from lang_proc import markovchain

class MarkovChainTests(unittest.TestCase):

    def test_single_sentence(self):
        """
        Tests with a single sentence
        """
        test_sentence = "This is sentence"
        a = markovchain.MarkovChain(1)
        a.train_paragraph(test_sentence)
        expected = {(): [(('This', 'DET'), 1)], (('sentence', 'NOUN'),): (), (('is', 'VERB'),): [(('sentence', 'NOUN'), 1)], (('This', 'DET'),): [(('is', 'VERB'), 1)]}
        self.assertEqual(expected, a.model)

    def test_single_sentence_harder(self):
        """
        Tests with a more difficult single sentence.
        """
        test_sentence = "Here is a bit longer sentence that I hope works correctly and gets me a good grade on my assignment."
        a = markovchain.MarkovChain(1)
        a.train_paragraph(test_sentence)
        expected = {(('grade', 'NOUN'),): [(('on', 'ADP'), 1)], (('correctly', 'ADV'),): [(('and', 'CONJ'), 1)], (('Here', 'ADV'),): [(('is', 'VERB'), 1)], (('longer', 'ADV'),): [(('sentence', 'NOUN'), 1)], (('good', 'ADJ'),): [(('grade', 'NOUN'), 1)], (('bit', 'ADV'),): [(('longer', 'ADV'), 1)], (('on', 'ADP'),): [(('my', 'PRON'), 1)], (('is', 'VERB'),): [(('a', 'DET'), 1)], (('I', 'PRON'),): [(('hope', 'VERB'), 1)], (('hope', 'VERB'),): [(('works', 'NOUN'), 1)], (('and', 'CONJ'),): [(('gets', 'VERB'), 1)], (): [(('Here', 'ADV'), 1)], (('assignment', 'NOUN'),): [(('.', '.'), 1)], (('gets', 'VERB'),): [(('me', 'PRON'), 1)], (('works', 'NOUN'),): [(('correctly', 'ADV'), 1)], (('that', 'ADP'),): [(('I', 'PRON'), 1)], (('my', 'PRON'),): [(('assignment', 'NOUN'), 1)], (('.', '.'),): (), (('sentence', 'NOUN'),): [(('that', 'ADP'), 1)], (('a', 'DET'),): [(('bit', 'ADV'), 1), (('good', 'ADJ'), 1)], (('me', 'PRON'),): [(('a', 'DET'), 1)]}
        self.assertEqual(expected, a.model)

    def test_multi_sentence(self):
        """
        Tests with a few sentences.:
        """
        test_paragraph = "This is sentence. I hope that it generates correctly. That would be nice."
        a = markovchain.MarkovChain(1)
        a.train_paragraph(test_paragraph)
        expected = {(('generates', 'VERB'),): [(('correctly', 'ADV'), 1)], (('it', 'PRON'),): [(('generates', 'VERB'), 1)], (('nice', 'ADJ'),): [(('.', '.'), 1)], (('hope', 'VERB'),): [(('that', 'ADP'), 1)], (('sentence', 'NOUN'),): [(('.', '.'), 1)], (('be', 'VERB'),): [(('nice', 'ADJ'), 1)], (('that', 'ADP'),): [(('it', 'PRON'), 1)], (('That', 'DET'),): [(('would', 'VERB'), 1)], (): [(('This', 'DET'), 1), (('I', 'PRON'), 1), (('That', 'DET'), 1)], (('would', 'VERB'),): [(('be', 'VERB'), 1)], (('This', 'DET'),): [(('is', 'VERB'), 1)], (('I', 'PRON'),): [(('hope', 'VERB'), 1)], (('.', '.'),): (), (('correctly', 'ADV'),): [(('.', '.'), 1)], (('is', 'VERB'),): [(('sentence', 'NOUN'), 1)]}
        self.assertEqual(expected, a.model)

    def test_higher_order_single_sentence(self):
        """
        Tests order 3 markov chain on a single sentence.
        """
        test_sentence = "Here is a bit longer sentence that I hope works correctly and gets me a good grade on my assignment."
        a = markovchain.MarkovChain(3)
        a.train_paragraph(test_sentence)
        expected = {(('Here', 'ADV'),): [(('is', 'VERB'), 1)], (('hope', 'VERB'), ('works', 'NOUN'), ('correctly', 'ADV')): [(('and', 'CONJ'), 1)], (('a', 'DET'), ('good', 'ADJ'), ('grade', 'NOUN')): [(('on', 'ADP'), 1)], (('on', 'ADP'), ('my', 'PRON'), ('assignment', 'NOUN')): [(('.', '.'), 1)], (('good', 'ADJ'), ('grade', 'NOUN'), ('on', 'ADP')): [(('my', 'PRON'), 1)], (('correctly', 'ADV'), ('and', 'CONJ'), ('gets', 'VERB')): [(('me', 'PRON'), 1)], (('a', 'DET'), ('bit', 'ADV'), ('longer', 'ADV')): [(('sentence', 'NOUN'), 1)], (('longer', 'ADV'), ('sentence', 'NOUN'), ('that', 'ADP')): [(('I', 'PRON'), 1)], (('and', 'CONJ'), ('gets', 'VERB'), ('me', 'PRON')): [(('a', 'DET'), 1)], (('that', 'ADP'), ('I', 'PRON'), ('hope', 'VERB')): [(('works', 'NOUN'), 1)], (('gets', 'VERB'), ('me', 'PRON'), ('a', 'DET')): [(('good', 'ADJ'), 1)], (('I', 'PRON'), ('hope', 'VERB'), ('works', 'NOUN')): [(('correctly', 'ADV'), 1)], (('me', 'PRON'), ('a', 'DET'), ('good', 'ADJ')): [(('grade', 'NOUN'), 1)], (('Here', 'ADV'), ('is', 'VERB')): [(('a', 'DET'), 1)], (('works', 'NOUN'), ('correctly', 'ADV'), ('and', 'CONJ')): [(('gets', 'VERB'), 1)], (('sentence', 'NOUN'), ('that', 'ADP'), ('I', 'PRON')): [(('hope', 'VERB'), 1)], (('my', 'PRON'), ('assignment', 'NOUN'), ('.', '.')): (), (('Here', 'ADV'), ('is', 'VERB'), ('a', 'DET')): [(('bit', 'ADV'), 1)], (('is', 'VERB'), ('a', 'DET'), ('bit', 'ADV')): [(('longer', 'ADV'), 1)], (): [(('Here', 'ADV'), 1)], (('bit', 'ADV'), ('longer', 'ADV'), ('sentence', 'NOUN')): [(('that', 'ADP'), 1)], (('grade', 'NOUN'), ('on', 'ADP'), ('my', 'PRON')): [(('assignment', 'NOUN'), 1)]}
        self.assertEqual(expected, a.model)