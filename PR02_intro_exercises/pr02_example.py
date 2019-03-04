'''
   DS2001 : PR 2 (SS) 
   Sample exercise: Eggs
   Jan 16, 2019

   ### Helpful links ###
   Style guide for DS 2000
   https://course.ccs.neu.edu/ds2000/styleguide.pdf
   
   Documentation on 'input' function
   https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html

'''

def main():
    """
        Parameters: none
        Returns: nothing
        Does: Prompts user for a number of eggs in dozens,
              returns total number of eggs
    """

    #Prompt user for input
    eggs_dozens = input('Enter number of eggs in dozens:')

    # force input to type 'int' and calculate number of single eggs
    eggs_single = int(eggs_dozens) * 12  

    print('you have', eggs_single, 'eggs') # final answer

main()





















#   print('You entered:', eggs_dozens) # checking input for example 
    
#    eggs_single = eggs_dozens * 12 # calculate number of single eggs
    
#    print('First guess', eggs_single) # checck output

#    print('Uhhhh...that is not right...') # panic

#    print('TYPE of input:', type(eggs_dozens)) # check type of input

#    print('ooooooh...Neet to convert to type int') 

    # force input to type 'int' and recalculate
#    eggs_single = int(eggs_dozens) * 12 

#    print('you have', eggs_single, 'eggs') #final answer
