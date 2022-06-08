import sys, pyperclip, cryptomath, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def getKeyParts(key):
    keyA, keyB = key//len(SYMBOLS), key%len(SYMBOLS)
    return keyA, keyB

def checkKeys(keyA, keyB, mode):
    if (keyA == 1 or keyB == 0) and mode == 'encrypt':
        sys.exit('Cipher is weak. Choose a different key')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between0 and % s.' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime.Choose a different key. ' % (keyA, len(SYMBOLS)))

def encrypt(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''.join([SYMBOLS[(SYMBOLS.find(symbol)*keyA+keyB)%len(SYMBOLS)] if symbol in SYMBOLS else symbol for symbol in message])
    return ciphertext

def decrypt(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''.join([SYMBOLS[(SYMBOLS.find(symbol) - keyB)*cryptomath.findModInverse(keyA, len(SYMBOLS))%len(SYMBOLS)] if symbol in SYMBOLS else symbol for symbol in message])
    return plaintext

def main(message, mode='encrypt'):
    key = 2894
    if mode == 'encrypt':
        translated = encrypt(key, message)
    if mode == 'decrypt':
        translated = decrypt(key, message)
    print('Key: %s' % (key))
    print('%sed text:' % (mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (mode))

myMessage = """A computer deserve to be called intelligent if it could deceive a human believing it was human.
- Alan Turing"""
encrypt_message = """5QG9ol3La6Qxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQda!AafARuQALQI1iQX3o1RN
-Q5!1RQP36ARu"""
main(encrypt_message, 'decrypt')