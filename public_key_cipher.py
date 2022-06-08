import sys, math

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
message = 'Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets. Gerald Priestland. The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people. Hugo Black.'


def main(message, mode='encrypt'):
    filename = 'encrypted_file.txt'
    if mode == 'encrypt':
        pubFilename = 'Boi_pubkey.txt'
        print('Encrypting and writing to %s...' % (filename))
        translated = encryptFile(filename, pubFilename, message)
    elif mode == 'decrypt':
        privFilename = 'Boi_privkey.txt'
        print('Reading from %s and decrypting...' % (filename))
        translated = decryptFile(filename, privFilename)
    print(f'{mode} text:')
    print(translated)

def text_to_blocks(message, blockSize):
    for character in message:
        if character not in SYMBOLS:
            print('ERROR: The symbol set does not have the character %s' % (character))
            sys.exit()
    blockInts = [sum([SYMBOLS.index(message[i])*len(SYMBOLS) ** (i % blockSize)
               for i in range(newBlock, min(newBlock + blockSize, len(message)))])
              for newBlock in range(0, len(message), blockSize)]
    return blockInts

def blocks_to_text(blockInts, messageLen, blockSize):
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLen:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer:
                charIndex = (blockInt // (len(SYMBOLS) ** i))
                blockInt = blockInt % (len(SYMBOLS) ** i)
                blockMessage.insert(0, SYMBOLS[charIndex])
        message.extend(blockMessage)
    return ''.join(message)

def encryptMessage(message, key, blockSize):
    n, e = key
    # ciphertext = plaintext ^ e mod n
    return [pow(block, e, n) for block in text_to_blocks(message, blockSize)]

def decryptMessage(encryptedBlocks, messagelen, key, blockSize):
    n, d = key
    return blocks_to_text([pow(block, d, n) for block in encryptedBlocks], messagelen, blockSize)

def readKeyFile(keyFilename):
    # Given the file name that contains public and private key
    # return the key as (n, e) or (n, d)
    with open(keyFilename, 'r') as fo:
        content = fo.read()
        keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))

def valid_key_size(keySize, blockSize):
    if not (math.log(2**keySize, len(SYMBOLS)) >= blockSize):
        sys.exit('ERROR: Block size is too large for the key and symbol set size. Did you specify the correct key file and encrypted file?')

def encryptFile(messageFile, keyFile, message, blockSize=None):
    # Using a key from key file, encrypt the message and save it to message file
    keySize, n, e = readKeyFile(keyFile)
    if blockSize == None:
        # If blockSize isnt given, set it to the largest size allowed
        blockSize = int(math.log(2**keySize, len(SYMBOLS)))
    # Check if key size is large enough for the block size:
    valid_key_size(keySize, blockSize)
    encryptedBlocks = encryptMessage(message, (n, e), blockSize)
    encryptedContent = ','.join([str(encryptedBlocks[i]) for i in range(len(encryptedBlocks))])
    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    with open(messageFile, 'w') as fo:
        fo.write(encryptedContent)
    return encryptedContent

def decryptFile(messageFile, keyFile):
    # Using the key from keyFile, read and decrypt encrypted message from messageFile
    keySize, n, d = readKeyFile(keyFile)
    with open(messageFile, 'r') as fo:
        content = fo.read()
        messageLen, blockSize, encryptedMessage = content.split('_')
        messageLen, blockSize = int(messageLen), int(blockSize)
    valid_key_size(keySize, blockSize)
    encryptedBlocks = [int(block) for block in encryptedMessage.split(',')]
    return decryptMessage(encryptedBlocks, messageLen, (n,d), blockSize)

if __name__ == '__main__':
    main(message, 'decrypt')

