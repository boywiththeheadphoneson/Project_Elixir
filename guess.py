#program to ask the user to guess a number between 1 - 100 and check if they have guessed it correctly

import random
num = random.randint(1, 100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')

print('if you gussed less than 6 times you won')
