import numpy as np
from common.util import *

text = "You say goodbye and I say hello."
corpus, word_to_id, id_to_word = preprocess(text)

print(corpus)
print(create_co_matrix(corpus, 7))
print(enumerate(corpus))

print(id_to_word)

