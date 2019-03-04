'''
   YOUR NAME HERE
   DS2001 : PR 5 (SS) 
   February 6, 2019

   == Exercise: Anscome's Quartet / Datasaurus Dozen ==

   ### End product ###
   - Read in all data from datasaurus.py
   - Calculate x_mean, y_mean, x_sd and y_sd for each set of coordinates
   - Print all 12 graphs to Turtle
       - Graphs should be different/random colors (at least 3 unique colors)
       - Graphs should be spaced out (3 rows of 4 plots)
   - Print x_mean, y_mean, x_sd and y_sd to Turtle

   ### Note: You may use whatever functions you want.
    # For your reference, I've included headers for the functions I used


   ### Suggested steps (Or follow your own!) ###
   1. Read the functions in datasaurus.py and visualize.py
   2. Start with a single plot from datasaurus.py
       -- Get plotting and calculating stats working
       -- Don't worry about adjusting plot position
       -- Tip: you can use any value of i to test write_stats()
   3. Try reading / plotting all coordinate sets
       -- Still don't worry about adjusting plot positions
          (This means everything will plot over each other)
   4. Use visualize.py functions to adjust plot positions
       -- No required order for plots
   5. Add color!
       -- Note: Points within a plot should be the same color
   

   ### Helpful links ###
   # Turtle named colors : https://trinket.io/docs/colors
'''


import datasaurus
import visualize
import math
import random # to randomize colors


def get_means(data):
  '''
    Parameters: data (list of floats)
    Returns: mean (float), of that list

    Does: Calculates the mean of a list of numbers
  '''


def get_sd(data, mean):
    '''
    Parameters: data (list of floats)
    			mean (float), of that list

    Returns: sd (float), of that list (eg, its standard deviation)

    Does: Calculates the standard deviation of a list of numbers
    	  (Standard deviation is first eaquation here: https://en.wikipedia.org/wiki/Standard_deviation)
    '''



def get_stats(coords):
    '''
    Parameters: coords, list of lists, with [float, float] as sublist

    Returns: x_mean, y_mean, x_sd, y_sd (all floats), summary statistics for those coordinates

    Does: Calculates the summary statistics for a plot
    '''



def adjust_coords(i, coords):
    '''
    Parameters: i (int), between 0-11 (inclusive)
    			coords, list of lists, with [float, float] as sublist

    Returns: new_coords, list of lists, with [float, float] as sublist

    Does: Adjusts all plot coordinates for canvass in position i
    '''



def main():
    '''
    Parameters: None

    Returns: None (will open Turtle screen)

    Does: Reads all plot data, calculates summary statistics, and draws/writes to Trurle screen
    '''

    # Tip: call a function from another file using:
    # filename.function_name()
    
    # be sure to pass any needed parameters and
    # assign the returned value to a variable if appropriate

main()
