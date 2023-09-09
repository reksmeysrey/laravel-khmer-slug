from khmernltk import word_tokenize
from khmernltk import sentence_tokenize
import unicodedata
import json
import sys
import re

# raw_text = "这是 段中文ខួបឆ្នាំទី២៨! asd,asdf.--=0-=@ 2342 sdaf/';''២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"

def main():
    run(sys.argv[1], sys.argv[2])
#     print(sys.argv[1])
#     print('\n')
#     print( sys.argv[2])
def slugify(value, allow_unicode=True):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def run(text: str, separator: str = "-"):
    string = word_tokenize(text, return_tokens=True)
#     return print(slugify(json.dumps(string, ensure_ascii=False).lower()))
    return print(json.dumps(string, ensure_ascii=False).lower())

if __name__ == '__main__':
    main()
