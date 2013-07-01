""" Input a word, check to be sure the word is alpha numeric 
    the convert the word to pyglatin
    """
pyg = 'ay'

original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print 'English word ' + word
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        new_word = word + pyg
        print 'PygLatin Translastion ' + new_word
    else:
        end = len(word)
        slice_word = word[1:end]
        new_word = slice_word + first + pyg
        print 'PygLatin Translation ' + new_word
else:
    print 'ERROR: empty word'
