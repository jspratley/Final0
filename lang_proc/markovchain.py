__author__ = 'Noel'

from lang_proc import nltktest
from random import randint
import nltk
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.tag import pos_tag, map_tag


class MarkovChain:

    n = 0
    model = {}
    type_model = {}
    type_frequencies = {}

    def __init__(self, n):
        if(n < 1):
            print("Error: Markov Chain should be of order 1 or higher. Creating an order 1 markov chain.")
        self.n = n

    def train_paragraph(self, paragraph):
        """
        Fills the state transition matrix using the paragraph provided.
        :param paragraph: paragraph to be trained on
        """
        sent_tokenize_list = sent_tokenize(paragraph)
        for sent in sent_tokenize_list:
             self.train(sent)

    def train(self, sent):
        """
        Single sentence will be used to fill the state transition matrix.
        :param sent: the sentence to be trained on
        """
        a = nltktest.tag_in_twos(sent)
        prev_list = ()
        for i in range(0, len(a)):
            if prev_list in self.model.keys():
                val_arr = self.model[prev_list]
                found = False
                for j in range(0, len(val_arr)):
                    if a[i] == val_arr[j][0]:
                        found = True
                        val_arr[j] = (val_arr[j][0], val_arr[j][1]+1)
                if not found:
                    self.model[prev_list].append((a[i], 1))
            else:
                self.model[prev_list] = [(a[i], 1)]
            prev_list = prev_list + tuple([a[i]])
            if(len(prev_list) > self.n):
                prev_list = prev_list[1:]
        self.model[prev_list] = ()


    def train_by_type_paragraph(self, paragraph):
        """
        Trains the markov chain on the types of each word.
        :param paragraph: the paragraph to be trained on
        """
        sent_tokenize_list = sent_tokenize(paragraph)
        for sent in sent_tokenize_list:
             self.train_by_types(sent)

    def add_type_frequencies(self, sent):
        a = nltktest.tag_in_twos(sent)
        # [TAG, TAG2, TAG3]
        for elem in a:
            if elem[1] in self.type_frequencies:
                val_arr = self.type_frequencies[elem[1]]
                found = False
                for i in range(0, len(val_arr)):
                    if elem[0] == val_arr[i][0]:
                        found = True
                        val_arr[i] = (val_arr[i][0], val_arr[i][1]+1)
                if not found:
                    self.type_frequencies[elem[1]].append((elem[0], 1))
            else:
                self.type_frequencies[elem[1]] = [(elem[0], 1)]
        print(self.type_frequencies)

    def train_by_types(self, sent):
        """
        trains a single sentence by the type value with the markov chain
        :param sent: the sentence to be trained on.
        """
        self.add_type_frequencies(sent)
        a = nltktest.get_tag_sequence(sent)
        prev_list = ()
        for i in range(0, len(a)):
            if prev_list in self.type_model.keys():
                val_arr = self.type_model[prev_list]
                found = False
                for j in range(0, len(val_arr)):
                    if a[i] == val_arr[j][0]:
                        found = True
                        val_arr[j] = (val_arr[j][0], val_arr[j][1]+1)
                if not found:
                    self.type_model[prev_list].append((a[i], 1))
            else:
                self.type_model[prev_list] = [(a[i], 1)]
            prev_list = prev_list + tuple([a[i]])
            if(len(prev_list) > self.n):
                prev_list = prev_list[1:]
        self.type_model[prev_list] = ()

        print(self.type_model)


    def choose_element(self, distribution):
        """
        chooses an element from a probability distribution.
        :param distribution:  the distribution to be chosen from
        """
        simulated_dist = []
        #print(distribution)
        for element in distribution:
            for i in range(0, element[1]):
                simulated_dist.append(element[0])
        #print(simulated_dist)
        if len(simulated_dist)-1 < 0:
            return None
        return simulated_dist[randint(0,len(simulated_dist)-1)]


    def generate_by_words(self):
        """
        generates using the word state transition matrix a sentence of 30 parts.
        """
        ret = ""
        prev_list = list(self.model.keys())[randint(0, len(list(self.model.keys()))-1)]
        print("---------GENERATION------------")
        for i in range(0, 30):
            current_distribution = self.model[prev_list]
            choice = self.choose_element(current_distribution)
            if(choice is not None):
                prev_list = prev_list + tuple([choice])
                if(len(prev_list) > self.n):
                    prev_list = prev_list[1:]
                ret += (str(choice[0]) + " ")
            else:
                prev_list = ()
        return ret

    def generate_by_types(self):
        """
        generates using the type state transition matrix a sentence of 30 parts.
        """
        ret = []
        prev_list = list(self.type_model.keys())[randint(0, len(list(self.type_model.keys()))-1)]
        print("---------GENERATION------------")
        for i in range(0, 30):
            current_distribution = self.type_model[prev_list]
            choice = self.choose_element(current_distribution)
            if(choice is not None):
                prev_list = prev_list + tuple([choice])
                if(len(prev_list) > self.n):
                    prev_list = prev_list[1:]
                ret.append(choice)
            else:
                prev_list = ()

        for i in range(0, len(ret)):
            current_distribution = self.type_frequencies[ret[i]]
            choice = self.choose_element(current_distribution)
            if choice is not None:
                ret[i] = choice

        print(ret)


def main():
    a = MarkovChain(3)
    sent = input("Please enter a sentence.")
    a.train_paragraph(sent)
    print(a.model)
    a.generate_by_words()
    a.generate_by_words()
    a.generate_by_words()
    a.generate_by_words()
    #a.train_by_types(sent)
    #a.generate_by_types()
    #print(a.generate_one())