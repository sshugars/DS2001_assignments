'''
   YOUR NAME HERE
   DS2001 : PR 3 (SS) 
   Jan 23, 2019

== (Modified) BlackJack ==
Prompt user to draw from a modifed deck of cards
Rules of deck:
* Produces a number between 1 and 10 (inclusive)
* Produces an infite number of cards of each value

User enters 'H' (hit) to recieve a new card and 'S' (stay) to stop

If user chooses H and has drawn a total strictly *greater than* 21
-> User loses

If user chooses H and receives a total of exactly 21
-> User wins

If user chooses S while total cards strictly *less than* 21
-> User wins if next card would put them over 21
-> User loses if next card would put them under or *equal to* 21

'''

import random

def hit():
    '''
        Parameters: None
        Returns: Value of card drawn
        Does: Draws a card
    '''


def end_game(total_points, action, card):
    '''
        Parameters: total_points (int), the total value the user has
                    action (str), the last action the user took
                    card (int), the value of the last card drawn
        Returns: None
        Does: Determines whether player wins or loses and prints message
    '''
     

def main():
    '''
        Parameters: None
        Returns: None
        Does: Main function
    '''

main()    

    ######### Sample output 1 ##########
    # Welcome to BlackJack!
    # Your first card is 4

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] Q
        # Entered value must be either 'H' or 'S'
        # [User Input:] H

    # Your new card is 8
    # Your total value is 12

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] H

    # Your new card is 10
    # Your total value is 22
    # BUSTED! You lose.



    ######### Sample output 2 #########
    # Welcome to BlackJack!
    # Your first card is 8

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] H

    # Your new card is 9
    # Your total value is 17

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] H

    # Your new card is 4
    # Your total value is 21
    # BlackJack! You win!


    ######### Sample output 3 #########
    # Welcome to BlackJack!
    # Your first card is 6

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] H

    # Your new card is 8
    # Your total value is 14

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] S

    # Next card would have been 9
    # That would have put you over 21!
    # You win!



    ######### Sample output 4 #########
    # Welcome to BlackJack!
    # Your first card is 2

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] H

    # Your new card is 3
    # Your total value is 5

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] H

    # Your new card is 1
    # Your total value is 6       

    # Enter 'H' to hit or 'S' to stay
        # [User Input:] S
          
    # Next card would have been 8
    # You should have hit to be closer to 21!'
    # You lose!
