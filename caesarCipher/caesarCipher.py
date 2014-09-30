from utils import paperclip

__author__ = 'xiaoyazi'

# Caesar Cipher


#the string to be encrypted/decrypted
message = 'This is my secret message.'

#the key to encrypton/decryption
key = 13

# encrypt or decrypte
mode = 'encrypt'

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the result message
translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol


print(translated)

paperclip.copy(translated)
