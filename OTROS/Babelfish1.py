
#!/usr/bin/python
# coding: utf-8

from sys import stdin


if __name__ == "__main__":

    word_dictionary = dict()

    for line in stdin:
        
        if len(line) == 1:
            break
        english_word, foreign_word = line.split()
        word_dictionary[foreign_word] = english_word


    for word in stdin:
        english_word = word_dictionary.get(word.rstrip())
        if not english_word:
            print("eh")
        else:
            print(english_word)


