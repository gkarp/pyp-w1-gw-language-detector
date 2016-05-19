# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES

def detect_language(text, languages):
    """Returns the detected language of given text."""
    textlist = text.split()
    result = {}
    for language in LANGUAGES:
        match = len([ x for x in textlist if x in language['common_words']])
        result[match] = language['name']
    mylang = result[max(list(result.keys()))]
    return mylang
    
#detect_language(text,LANGUAGES)




