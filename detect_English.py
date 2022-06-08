AlPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import re
def loadDict():
    english_words = {}
    with open('dictionary.txt', 'r') as fobj:
        for word in fobj.read().split('\n'):
            english_words[word] = None
    return english_words

ENGLISH_WORDS = loadDict()
letter = re.compile(r'[^A-Za-z0-9 ]+')

def get_freq(message):
    message = letter.sub('', message).upper()
    words = message.split()
    if words == []:
        return 0.0
    matches = 0
    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1
    return matches/len(words)*100

def isEnglish(message, wordPercent=20, letterPercent=85):
    match_words = get_freq(message) >= wordPercent
    numLetters = len(letter.sub('', message))
    match_letters = numLetters/len(message)*100 >= letterPercent
    return match_words and match_letters

if __name__ == '__main__':
    print(isEnglish(('Is this sentence English text?')))
