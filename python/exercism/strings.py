"""Functions for creating, transforming, and adding prefixes to strings."""

import string

def add_prefix_un(word: str) -> str:
    return 'un' + word

def make_word_groups(vocab_words: list[str]) -> str:
    words = ([word if idx == 0 else vocab_words[0] + word
              for idx, word in enumerate(vocab_words)])
    return str.join(' :: ', words)

def remove_suffix_ness(word: str) -> str:
    word = word[:-4]
    if word[-1] == 'i': word = word[:-1] + 'y'
    return word

def adjective_to_verb(sentence: str, index: int) -> str:
    translation_table = str.maketrans(dict.fromkeys(string.punctuation))
    word = sentence.split(' ')[index].translate(translation_table)
    return word + 'en'
