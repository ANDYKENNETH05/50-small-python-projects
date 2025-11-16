print('caesar Cipher Hacker, by AI Sweigart Al@inventWithpyhon')
print('Enter the encrypted Ceasar cipher message to hack.')
message = input('> ')
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range(len(SYMBOLS)):
    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(SYMBOLS)
                translated = translated + SYMBOLS[num]
            else:
                translated = translated + symbol

    print("key #{}: {}".format(key, translated))