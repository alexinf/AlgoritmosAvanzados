
#!/usr/bin/python
# coding: utf-8
from sys import stdin

dictionary = dict()

for text in stdin:
	if len(text) == 1:
		break
	english, native = text.split()
	dictionary[native] = english

for traslate in stdin:
	english = dictionary.get(traslate.rstrip())
	if not english:
		print("eh")
	else:
		print(english)