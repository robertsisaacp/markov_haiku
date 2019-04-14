"""
[x] Import count_syllables module
[x] Load a training-corpus text file
[x] Process the training corpus for spaces, newline breaks, and so on
"""
from count_syllables import count_syllables
from collections import defaultdict

# Test count_syllables()
with open('train.txt', 'r') as f:
    corpus = f.read().split()

TEST_WORDS = ["test", "wordless", "movement"]
print("---")
print("Syllable Test")
for word in TEST_WORDS:
    print(f"    Word: '{word}', syllables: '{count_syllables(word)}'")
print("---")

"""
[x] Map each word in corpus to the word after (Markov model order 1)
[x] Map each word pair in corpus to the word after (Markov model order 2)
[ ] Give user choice of generating full haiku, redoing lines 2 or 3, or exiting
"""

"""
nums = list(range(1, 100 + 1))

words = corpus[:10]
print(words)

o_1, o_2 = defaultdict(list), defaultdict(list)

for a, b, c in zip(words, words[1:], words[2:]):
    # print(a, b, c)
    o_1[a].append(b)
    o_2[a, b].append(c)
    # print(a, b)

print(o_1)
print(o_2)
"""

order_1, order_2 = defaultdict(list), defaultdict(list)


for first, second, third in zip(corpus, corpus[1:], corpus[2:]):

    order_1[first].append(second)

    # order_2[first, second].append(third)
    # TODO: account for end of list

    # Build markov chain order 2
    if (first, second) in order_2:
        order_2[first, second].append(third)
    else:
        order_2[first, second] = [third]


print(list(zip(corpus, corpus[1:])))
# print(order_2)

# if first in order_1:
#     order_1[first].append(second)
# else:
#     order_1[first] = [second]
# print(order_1['voicing'])
# print((order_2['of', 'the']))

# print(len(order_1))
# print(len(order_2))
# print(order_1)
# print(order_2)

# print(len(corpus))
# print(len(set(corpus)))
# print(corpus[-1])


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
