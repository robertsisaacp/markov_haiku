"""  # {{{
[x] Import count_syllables module
[x] Load a training-corpus text file
[x] Process the training corpus for spaces, newline breaks, and so on
[x] Map each word in corpus to the word after (Markov model order 1)
[x] Map each word pair in corpus to the word after (Markov model order 2)
[ ] Give user choice of generating full haiku, redoing lines 2 or 3, or exiting

"""  # }}}

from collections import defaultdict
from count_syllables import count_syllables
import random

# Build markov dictionaries
with open('train.txt', 'r') as f:
    CORPUS = f.read().split()
ORDER_1, ORDER_2  = defaultdict(list), defaultdict(list)
for first, second, third in zip(CORPUS, CORPUS[1:], CORPUS[2:]):
    ORDER_1[first].append(second)
    ORDER_2[first, second].append(third)


def new_line(seed_word="", line_length=5):
    first_word = seed_word if seed_word else random.choice(CORPUS)
    second_word = random.choice(ORDER_1.get(first_word))
    words = [first_word, second_word]

    print(words)
    syllables = count_syllables(" ".join(words))

    count = 0
    while syllables != line_length and count < 10:
        count = count + 1
        random.shuffle(ORDER_2.get((first_word, second_word)))
        # word = random.choice(ORDER_2.get((first_word, second_word)))
        for word in ORDER_2.get((first_word, second_word)):
            print(word)

        # if (syllables + count_syllables(word)) <= 5:
        #     words.append(word)
        #     syllables = syllables + count_syllables(word)
        #     first_word = second_word
        #     second_word = word

    # third_word = ""
    # while not third_word:
    #     if (seed_word, second_word) in ORDER_2:
    #         third_word = random.choice(ORDER_2[seed_word, second_word])
    # "".join([])
    return " ".join(words)


print(new_line())


"""
If first line:
    Target syllables = 5
    Get random word from corpus <= 4 syllables (no 1-word lines)
    Add word to line
    Set random word = prefix variable
    Get mapped words after prefix
    If mapped words have too many syllables
        Choose new prefix word at random & repeat
    Choose new word at random from mapped words
    Add the new word to the line
    Count syllables in word and calculate total in line
    If syllables in line equal target syllables
        Return line and last word pair in line
Else if second or third line:
    Target = 7 or 5
    Line equals last word pair in previous line
    While syllable target not reached:
        Prefix = last word pair in line
        Get mapped words after word-pair prefix
        If mapped words have too many syllables
            Choose new word-pair prefix at random and repeat
        Choose new word at random from mapped words
        Add the new word to the line
        Count syllables in word and calculate total in line
        If total is greater than target
            Discard word, reset total, and repeat
        Else if total is less than target
            Add word to line, keep total, and repeat
        Else if total is equal to target
            Add word to line
    Return line and last word pair in line
Display results and choice menu

"""
