# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:00:36 2019

@author: positiveoutlier

Move the first letter of each word to the end of it, then add "ay" to the end
of the word. Leave punctuation marks untouched.
    Expected input:   string
    Expected output:  string
"""


def pig_it(text):
    wordList = text.split()
    newList = []
    for word in wordList:
        if word.isalpha():
            word = word[1:] + word[:1] + "ay"
        newList.append(word)
    return print(" ".join(newList))


pig_it('Pig latin is cool yes !')


# with list comprehension
def pig_it2(text):
    wordList = text.split()
    newList = [((word[1:] + word[:1] + "ay") if word.isalpha() == 1 else word)
               for word in wordList]
    return print(" ".join(newList))


pig_it2('Pig latin is cool yes !')
