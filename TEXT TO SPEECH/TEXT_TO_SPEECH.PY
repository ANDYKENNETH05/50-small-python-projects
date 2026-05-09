"""Text To Speech Talker, by Al Sweigart al@inventwithpython.com
 An example program using the text-to-speech features of the pyttsx3
 module.
 Tags: tiny, beginner"""


import sys

try:
    import pyttsX3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this program')
    print('On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()

tts = pyttsX3.init()

print('Text To Speech Talker, by Al Sweigart al@inventwithpython.com')
print() 
print('Enter the text to speak, or QUIT to quit.')

while True:
    text = input("> ")
    if text.upper()== 'QUIT':
        print('thanks for playing!')
        sys.exit()

    tts.say(text)
    tts.runAndWait()
