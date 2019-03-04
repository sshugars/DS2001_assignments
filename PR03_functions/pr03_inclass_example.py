'''
   DS2001 : PR 3 (SS) 
   Sample exercise: Drama of the Commons
   Jan 23, 2019

   This game plays a "drama of the commons" game about over-fishing.
   You and I are both fisher-people.
   We both want as many fish as possible!
   But we don't want to run out of fish.

   The game will start with a random number of fish 
   and go on for a random number of rounds 

   Each round, you and I will go fishing in a random order.
   We will try to out-fish each other without removing all the fish.

   At the end of each round, the number of fish will double.
   
   END CONDITIONS:
   If there are no fish left in the sea, we both lose.

   If there are fish in the sea at the end of the final round
   the player with the most fish wins.


   ### Helpful links ###
   Style guide for DS 2000
   https://course.ccs.neu.edu/ds2000/styleguide.pdf
'''

import random
import math


def init_game():
    '''
        Parameters: None
        Returns: current_fish (int), total_rounds (int)
        Does: Initalizes game by selecting random numbers
            for the starting number of fish and
            total rounds to play for
    '''
        
    current_fish = random.choice(range(10, 21)) ### WHAT VALUES CAN THIS TAKE?
    total_rounds = random.choice(range(5, 11)) ### WHAT VALUES CAN THIS TAKE?

    print('New game starting...')

    return current_fish, total_rounds


def user_fishes(current_fish):
    '''
        Parameters: current_fish (int), the number of fish currently in the sea 
        Returns: your_fish (int), the number of fish you caught this turn
        Does: Prompts user for valid input of # of fish to catch
    '''
    
    #prompt user for input
    your_fish = int(input('How many fish do you want to catch?\n'))

    #check for valid input and reprompt if necessary
    while your_fish < 0 [AND/OR ?? ] your_fish > current_fish: ### WHAT CONDITION DO WE WANT HERE?
        
        print('Must be a value betweent 0 and ', current_fish)
        your_fish = int(input('How many fish do you want to catch?\n'))

    return your_fish


def computer_fishes(current_fish):
    '''
        Parameters: current_fish (int), the number of fish currently in the sea 
        Returns: my_fish (int), the number of fish I caught this turn
        Does: Goes fishing for the computer
    '''

        # Computer will select a number of fish 
        # between 1/4 and 3/4 of the current_fish population
        
        quarter = math.ceil(current_fish / 4) #round up
        three_quarters = min([quarter * 3, current_fish + 1])  #### MIN / MAX functions

        my_fish = random.choice(range(quarter, three_quarters))
        # NOTE: range() includes v1, excludes v2

        return my_fish


def update_fish(current_fish, player_fish, player_total_fish):
    '''
        Parameters: current_fish (int), number of fish in the sea *before* player turn
                    player_fish (int), # of fish caught this turn
                    player_total_fish (int), player's total fish *before* player turn
                    
        Returns: current_fish (int), number of fish in the sea *after* player turn
                  player_total_fish (int), player's total fish *after* player turn
        
        Does: Updates the current_fish and player_fish values to refect turn
    '''
    
    current_fish -= player_fish         #### += / -= NOTATION
    player_total_fish += player_fish

    return current_fish, player_total_fish

   
def play_round(players, current_fish, your_total_fish, my_total_fish):
    '''
        Parameters: players (list), a list of players in the game
                    current_fish (int), number of fish in the sea *before* turns
                    your_total_fish (int), number of fish you have *before* turn
                    my_total_fish (int), number of fish I have *before* turn
        
        Returns: current_fish (int), number of fish in the sea *after* turns
                 your_total_fish (int), number of fish you have *after* your turn
                 my_total_fish (int), number of fish I have *after* my turn
        
        Does: determines player order and executes player turns
    '''
    
    # randomize player order
    random.shuffle(players)
    #NOTE: random.shuffle() executes *in place* and overwrites old list
    

    #players take their turns fishing
    for player in players:

        # WHAT IF THE FIRST PLAYER TAKES ALL THE FISH?
        #
        #
        #

        # take your turn
        if player == 'you':
            print('\nCurrent Fish in Sea:', current_fish, \
            '\nYou have', your_total_fish, 'fish' \
            '\nI have', my_total_fish, 'fish')
                
            your_fish = user_fishes(current_fish)
            
            current_fish, your_total_fish = \
                          update_fish(current_fish, \
                                      your_fish, \
                                      your_total_fish)
                
            print('You catch', your_fish, 'fish')

        # take my turn
        if player == 'me':
            my_fish = computer_fishes(current_fish)
                
            current_fish, my_total_fish = \
                          update_fish(current_fish, \
                                      my_fish, \
                                      my_total_fish)
                
            print('I catch', my_fish, 'fish')

    return current_fish, your_total_fish, my_total_fish



def end_game(current_fish, your_total_fish, my_total_fish):
    '''
        Parameters: current_fish (int), number of fish in the sea at end game
                    your_total_fish (int), number of fish you have at end game
                    my_total_fish (int), number of fish I have at end game
        Returns: None
        Does: Determines and prints end-game conditions
    '''
        
    if current_fish == 0:
        print('\nECOLOGICAL DISASTER! No fish left. We all lose :(')
        
    else:
        print('\nECOSYSTEM SUSTAINED!', current_fish, 'fish left.' \
              '\nYou have', your_total_fish, 'fish' \
              '\nI have', my_total_fish, 'fish')
        
        if your_total_fish > my_total_fish:
            print('You win at fishing! Congratulations!')
        elif my_total_fish > your_total_fish:
            print('I caught more fish! I win! Yay for me.')
        else:
            print('Whoa, we got the same number of fish!')

    return None

def main():
    '''
        Parameters: None.
        Returns: None.
        Does: Initalizes and plays fishing game!
    '''

    #initalize parameters
    current_round = 0
    your_total_fish = 0
    my_total_fish = 0
    players = ['you', 'me']

    current_fish, total_rounds = init_game()

    while current_fish > 0 [AND/OR ??? ] current_round < total_rounds:  ### WHAT CONDITION DO WE WANT HERE?
        
        print('\n********Round:', current_round, '********')
        
        current_fish, your_total_fish, my_total_fish = \
                      play_round(players, current_fish, \
                                 your_total_fish, my_total_fish)
                
        #fish spawn -- double at the end of each round
        current_fish = current_fish * 2
        
        ### HOW DO WE MAKE SURE WE'RE NOT IN AN INFITE LOOP?
        ### INFITE LOOPS ARE BAD


    # Determine end game conditions
    end_game(current_fish, your_total_fish, my_total_fish)

main()

