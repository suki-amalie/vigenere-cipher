from transposition_cipher import decrypt
from detect_English import isEnglish
import pyperclip

def hack(message):
    print('Hacking...')
    print('Press Ctrl-C to quit at any time.')
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))
        decrypted = decrypt(message, key)
        if isEnglish(decrypted):
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decrypted[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')
            if response.upper().startswith('D'):
                return decrypted
    return None

def main():
    myMessage = """AaKoosoeDe5 b )alat r lw o
dh gaecnpeutaa e  enlh na 
lhetcdba. t t rsfcegru ieu v er Ne  nitiaicynhr aBercaeu thllE.no euarisf gmnoa yc r,ie d iorr.gAnlnoe(c -or1w shcnth  ek ra'lhlrrceey
n one dtes i o d ro hAe snretrm audg,tfl1e1 v
8aEheideikfr  lbsya apor t gHt nie cetr riebruaisss 
edhsppmsa- e a0m82e 5sn ma reno o eb  nglom,Ai ieetgn iodhs indeit n uho g eturmt NCsLc b17m 2 gmanw,forwnCsaemie-sp nc nrshicwsg etatt  e mealef aa  toe"""

    hacked = hack(myMessage)
    if hacked == None:
        print('Failed to hack encryption')
    else:
        print('Copying hacked message into clipboard...')
        print(hacked)
        pyperclip.copy(hacked)

main()



