import sys, random
import time 

assert sys.version_info >= (3,7), "This script requires at least Python 3.7" 

print ('While venturing through the woodlands of Carpathia, you encounter a horrible wizard.')
input('Press ENTER to continue...')

print ('"If you do not wish to perish, then you must accept my challenge."')
input('Press ENTER to continue...')

print ('"You have 5 rounds to guess a number between 1 and 30. After 5 rounds, I get to eat you."')

def number_guessing_game(low, high, rounds):
    number = random.randint(1, 30)
    Turns =0

    for _ in range(rounds):
            guess = input("GUESS A NUMBER: ")
            Turns +=1
    
            try:
                integer = int(guess)
                if integer == number:
                    print('"Fine, you win!!!" The wizard lets you free.')
                    print("Number of turns used: ",Turns)
                    return
                elif integer < number:
                    print('Try higher, mortal')
                elif integer > number:
                    print('Try lower...')

            except ValueError:
                print("This counts as a guess. You must enter a whole number or the wizard will kill you.")

    print("You didn't guess correctly in five rounds. The wizard eats your flesh.")

number_guessing_game(1, 30, 5)
