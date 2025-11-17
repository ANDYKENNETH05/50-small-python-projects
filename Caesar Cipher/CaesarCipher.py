# moreinfo at : https://nostarch.com/big-book-small-python-projects

try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')

print()
while True:
    print("do you want to (e)ncrypt or (d)encrypt: ")
    response = input('> ').lower()
    if response.startswith("ed"):
        mode = 'run code'
        print("run code and input e or d")
        break
    if response.startswith('e'):
        mode = 'encrypt'
        break
    if response.startswith("de"):
        mode = ('run code again')
        print('code finished, Run code again')
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('please enter the letter d or e.')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
print ("Enter the message to {}.".format(mode))
message = input('> ')
message = message.upper()

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol
        print(translated)

try:
    pyperclip.copy(translated)
    print('full {}ed text copied to clipboard.'.format(mode))
except:
    pass