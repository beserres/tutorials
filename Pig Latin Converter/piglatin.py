pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print first
    if first in ["a", "e", "i", "o", "u"]:
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + word[0] + pyg
        print new_word
else:
    print 'empty'