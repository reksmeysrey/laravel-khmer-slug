# -*- coding: UTF-8 -*-
from khmernltk import word_tokenize
from khmernltk import sentence_tokenize
from khmernltk import pos_tag
import json

text = 'ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្'

# sentence tokenization
result = sentence_tokenize(text)
print(result)
# write to a file if you have trouble reading the output in console
#with open('temp.txt', 'a', encoding='utf8') as f:
#    f.write(json.dumps(result, ensure_ascii=False) + '\n')


# word tokenization
result = word_tokenize(text, return_tokens=True)
print(result)
# remove white space from the output list
#result = [x for x in result if x != ' ']
#print(result)

# POS taggin
result = pos_tag(text)
print(result)
