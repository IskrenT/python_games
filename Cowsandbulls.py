## Software: Cowsandbulls Copyright (C) 2017 Iskren Tarkalanov
## Authors: Iskren Tarkalanov
## Language: Python
## Description: A console implementation of the game "Cows and Bulls".
##
## Cowsandbulls is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## any later version.
##
## Cowsandbulls is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## See <http://www.gnu.org/licenses/> to obtain full license.
##
##  Contact: isktark@yahoo.com Iskren Tarkalanov

def digit_repeat( num ): # Checks if the number has repeating digits
    test_number = ["0","0","0","0","0","0","0","0","0","0"]
    for i in range(len(num)):
        if(test_number[int(num[i])] == "1"):
            return True
        else:
            test_number[int(num[i])] = "1"
    return False

def is_integer( num ):
    for i in range(len(num)):
        if( num[i] < '0' or num[i] > '9' ):
            return False
    return True

import random
new_game = "n"

while(new_game == "n"):# Main program loop
    print("Cows and Bulls game, guess my randomly generated number!")
    hidden = "00"
    while ( digit_repeat( hidden ) ):# Cycle until generated number has distinct digits
        hidden = str(random.randint(1023,9876))
    while ( True ):
        num = input("Enter your guess: ")
        ## Testing for wrong input
        if ( not is_integer(num) ):
            print("Please input integer numbers only")
            continue
        if ( int(num) > 9876 or int(num) < 123 ):
            print("Your number should be between 0123 and 9876")
            continue
        if ( digit_repeat( num ) == True ):
            print("Your number should have distinct digits")
            continue
        ## Actual algorithm begins
        cows = 0
        bulls = 0
        for i in range(len(num)):
            if num[i] == hidden[i]:
                bulls = bulls + 1 #or bulls += 1
            elif num[i] in hidden:
                cows = cows + 1
        print("Bulls: ",bulls," Cows: ",cows)
        if( bulls == 4 ):
            print("Congratulations, YOU WON!")
            break
    new_game = "False"
    new_game = input("Enter 'n' for a new game: ")
