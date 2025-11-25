"""cho-han by AI Sweigart"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''JAPANESE dice game,two dice are rolled and 
      the player must guess if the dice rolled is total to an even (cho) of odd (han) number.
       ''')

purse = 5000

while True:
    print('you have', purse ,'mon. How much do you want to bet? (or QUIT)')
    while True:
        pot = input ('> ')
        if pot.upper() == "QUIT":
            print('thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('please enter a number.')
        elif int(pot) > purse:
            print('you do not have enough to make a bet.')
        else:
            pot = int(pot)
            break


    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    print('the dealer swirls the cup and and you hear he rattle of dice.')
    print('the dealer slams the cup on the floor, sill covering the')
    print('dice and asks for your bet.')
    print()
    print(' CHO (even) or HAN(odd)?')

    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('please enter either "CHO" or "HAN". ')
            continue
        else:
            break
    print('The dealer lifts the cup to reveal:')
    print(' ',JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print(' ', dice1, '-',dice2)

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
    
    playerWon = bet == correctBet

    if playerWon:
        print('yoou won! you take', pot, 'mon.')
        purse = purse + pot
        print('the house collects a', pot // 10, 'mon fee.')
        purse = purse - (pot // 10)
    else:
        purse = purse - pot 
        print('you lost')
    
    if purse == 0:
        print('you have run out of money!')
        print('thanks for playing')
        sys.exit()