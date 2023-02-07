# import list that I want to use

with open('answers.txt') as file:
    possible_answers = file.readlines()

list_possible_answers = sorted([re.sub(r'[^A-Z]', '', t.upper()) for t in possible_answers[0].split(',')])
print(len(list_possible_answers),
      list_possible_answers[:5])

# wordle solver v1, do it based off of letter frequency

# wordle solver v2, randomize my guess at the beginning

# wordle solver v3

