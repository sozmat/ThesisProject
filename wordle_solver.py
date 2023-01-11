# Wordle Solver Honors Thesis project

import string
import re
import numpy as np
import pandas as pd

# open text file that has possible answers
with open('answers.txt') as file:
    possible_answers = file.readlines()

list_possible_answers = sorted([re.sub(r'[^A-Z]', '', t.upper()) for t in possible_answers[0].split(',')])
print(len(list_possible_answers),
      list_possible_answers[:5])

# arrange as a DataFrame
arr_words_5l = np.array([list(w) for w in list_possible_answers])
df_words_5l = pd.DataFrame(data=arr_words_5l,columns=[f'letter_{i+1}' for i in range(5)])
df_words_5l['word'] = list_possible_answers
df_words_5l.head()

class Game:

    def __init__(self, df_all_5l_words):

        # Start with whole alphabet as list of possible letters in word
        self.possible_letters = list(string.ascii_uppercase)

        # To store guessed letters that are correct, but in the wrong location
        self.dict_misplaced_letters = Counter()

        # Possible answers
        self.df_possible_5l_words = df_all_5l_words.copy(deep=True)

        # Dictionary of answers, initialized as empty
        self.dict_letters = defaultdict(str)
        for i in range(5):
            self.dict_letters[i+1] = None

        # Initialize dictionary of letter counts at each position, updated as we play the game
        self.dict_letter_counts = defaultdict(str)
        for i in range(5):
            self.dict_letter_counts[i+1] = Counter(df_all_5l_words[f'letter_{i+1}'])

