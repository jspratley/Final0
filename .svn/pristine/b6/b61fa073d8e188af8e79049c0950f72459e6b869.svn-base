__author__ = 'Noel'

import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import treebank
from nltk.tag import pos_tag, map_tag

"""
sentence = ""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
print(tagged[0:6])

#entities = nltk.chunk.ne_chunk(tagged)
#print(entities)
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
"""
lexicon = {}


#Have a description for NNS go to Noun for example. Create larger buckets for types. Can do.
#Eliminate plural words if possible????????????????????????????????????????????????????????????????????????????????????????????????????????????????
#Decide whether to keep punctuation. Probably keep it.
#Filter out punctuation on display.


#Reference: http://stackoverflow.com/questions/5787673/python-nltk-how-to-tag-sentences-with-the-simplified-set-of-part-of-speech-tags
def add_sentence(sent):
    """
    Takes in a sentence and adds it to the lexicon.
    Example:
        Input:
            "These are a bunch of words to be processed"
        Tagged:
            {'VERB': ['are', 'be', 'processed'], 'ADP': ['of'], 'NOUN': ['bunch', 'words'], 'DET': ['these', 'a'], 'PRT': ['to']}
    :param sent: A sentence to be processed, tagged, and placed in the lexicon
    """
    mytok = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(mytok)
    tags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tags]

    # Place the word (converted to lower case) in the correct tag category.
    for key in tags:
        if key[1] in lexicon:
            if key[0] not in lexicon[key[1]]:
                lexicon[key[1]].append(key[0].lower())
        else:
            lexicon[key[1]] = [key[0].lower()]


def main():
    sent = input("Enter a paragraph: ")
    sent_tokenize_list = sent_tokenize(sent)
    for s in sent_tokenize_list:
        add_sentence(s)
    print(lexicon)



main()