__author__ = 'Noel'

import nltk
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.tag import pos_tag, map_tag

def place_tagged_in_lexicon(tags, lexicon):
    """
    Place the word (converted to lower case) in the correct tag category.
    :param tags: The sentence, parsed and tagged.
    Example Input:
        {'VERB': ['are', 'be', 'processed'], 'ADP': ['of'], 'NOUN': ['bunch', 'words'], 'DET': ['these', 'a'], 'PRT': ['to']}
    This input will then be placed in the lexicon in the correct categories.
    """
    for key in tags:
        if key[1] in lexicon:
            if key[0] not in lexicon[key[1]]:
                lexicon[key[1]].append(key[0].lower())
        else:
            lexicon[key[1]] = [key[0].lower()]


#Reference: http://stackoverflow.com/questions/5787673/python-nltk-how-to-tag-sentences-with-the-simplified-set-of-part-of-speech-tags
def add_sentence(sent, lexicon):
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
    place_tagged_in_lexicon(tags, lexicon)



def add_sentence_complex(sent, lexicon):
    """
    Takes in a sentence and adds it to the lexicon, but using complex tags.
    Example:
        Input:
            "These are a bunch of words to be processed"
        Tagged:
            {'NNS': ['words'], 'NN': ['bunch'], 'VBN': ['processed'], 'VBP': ['are'], 'DT': ['these', 'a'], 'VB': ['be'], 'IN': ['of'], 'TO': ['to']}
    :param sent: A sentence to be processed, tagged, and placed in the lexicon
    """
    mytok = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(mytok)
    place_tagged_in_lexicon(tags, lexicon)



def add_paragraph(paragraph, lexicon):
    """
    Will take a in a paragraph, and place each sentence into the lexicon.
    See add_sentence.
    """
    sent_tokenize_list = sent_tokenize(paragraph)
    for s in sent_tokenize_list:
        add_sentence(s, lexicon)

def add_paragraph_no_punctuation(paragraph, lexicon):
    """
    Will take a in a paragraph, and place each sentence into the lexicon.
    Removes punctuation from the string. See add_sentence.
    NOTE: Contractions are an issue with this.
    """
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized= tokenizer.tokenize(paragraph)
    tags = nltk.pos_tag(tokenized)
    tags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tags]
    place_tagged_in_lexicon(tags, lexicon)

def create_structure_from_sentence(sentence):
    """
    Creates the dictionary for the visualization.

    :param sentence: A sentence to be reformatted
    :return: visualization structure
    """
    temp_lex = {}
    temp_lex["children"] = {}
    add_sentence(sentence, temp_lex["children"])
    lexicon = {'name': 'lexicon', 'children': []}
    new_char_list = [x for x in temp_lex["children"].keys()]
    words_by_type = [temp_lex["children"][x] for x in new_char_list]

    #words_by_type = [["Word", "Letters"], ["More", "Another"]]
    for i in range(len(new_char_list)):
        type_dict = {'name': new_char_list[i], 'children': []}
        for a in words_by_type[i]:
            type_dict['children'].append({'name': a})
        lexicon['children'].append(type_dict)
    return lexicon

def tag_in_twos(sent):
    """
    Tags the sentence in the traditional nltk method.
    Example:
        Input:
            These are words
        Output:
            [('These', 'DET'), ('are', 'VERB'), ('words', 'NOUN')]
    :param sent: A sentence to tag
    :return: words and their tags.
    """
    mytok = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(mytok)
    tags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tags]
    return tags


def print_words_in_lexicon(lexicon):
    """
    Prints all words contained in the lexicon currently.

    Example:
        Lexicon contents:
            {'ADP': ['that'], 'ADV': ['properly'], 'VERB': ['hope', 'works'], 'PRON': ['i'], 'DET': ['this']}
        Output:
            ADP:
                that
            ADV:
                properly
            VERB:
                hope
                works
            PRON:
                i
            DET:
                this
    """
    print(lexicon)
    for key in lexicon:
        print(key + ":")
        for element in lexicon[key]:
            print("\t" + str(element))

def get_tag_sequence(sent):
    """

    :param sent: A sentence to tag
    :return: Tags in order.
    """
    mytok = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(mytok)
    tags = [map_tag('en-ptb', 'universal', tag) for word, tag in tags]
    return tags


def main():
    """
    For testing purposes.
    """
    lexicon = {}
    sent = input("Enter a paragraph: ")
    add_sentence_complex(sent, lexicon)
    print_words_in_lexicon(lexicon)