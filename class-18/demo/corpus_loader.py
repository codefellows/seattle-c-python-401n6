# lzw
# the shift of 8
# shift of 1 -> max
# ske qudhs ldcuhe kshdb
# the lasdu dkhadd lsieh Shift of 2
# max roger wounds blood shift 8
# pip install nltk
import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()
# print(word_list)

word = 'the quick brown fox'

if word in word_list:
    print('It is there!')
else:
    print('It is not there!')
