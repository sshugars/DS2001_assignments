'''
   YOUR NAME HERE
   DS2001 : PR 6 (SS) 
   February 13, 2019

   == Exercise: Fatal Encounters with Police (US) ==
   Following the fatal shooting of Michael Brown in Ferguson, Mo.
   on Aug. 9, 2014, there has been increased attention on collecting and
   analyzing data related to fatal police encounters in the US. 

   You can read more about the dialogue around this issue and
   specific cases which have raised questions about officer conduct here:
   https://www.nytimes.com/interactive/2015/04/08/us/fatal-police-shooting-accounts.html

   ### Data details ###
   These data were downloaded from:
   https://www.kaggle.com/kwullum/fatal-police-shootings-in-the-us

   There are two data files:
   == state_population.csv ==
      First row contains header
      Each row contains a state name followed by
           the share of the population of a given racial category
      
   Columns are:
       state, white, black, native_american, asian,hispanic

   == fatal_police_encounters.csv ==
      First row contains header
      Each row contains a record of a fatal encounter with a police officer
      Covers Jan 2015 - July 2017

  Columns are:
      name, date, age, gender, race, city, state
      
      date is formatted dd/mm/yy
      age recorded as '' if missing
      gender is only recorded as a binary with options 'M' and 'F'
      race recorded as 'white', 'black', 'native_american', 'asian',
          'hispanic', or 'other'
   

   ### End product ###
   Provide answers to the following questions using the
   data from state_population.csv and fatal_police_encounters.csv
   (Answers can be copy and pasted into the bottom of your code)

   (1a) Print the name every person killed in a police encounter
       to your screen.
   (1b) How many people are listed in this dataset? 
   (2) What percentage of fatalities were male?
   (3) What is youngest, oldest, and average age in the dataset

   (4) For THREE states of your choosing, calculate:
       (a) the population share for each demographic category
       (b) the fatality share for each demographic category
       NOTE: the fatality dataset includes 'other' which is not in the
             population dataset. You don't need to report this, and
             your values may not add up to 100% as a result.rfg

   Here's the calculation for Massachusetts:
   White : 89.3% (population share)
           45.4% (fatal encounter share)
           
   Black : 2.79% (population share)
           31.8%  (fatal encounter share)
           
   Native American : 0.27% (population share)
                     0% (fatal encounter share)
   Asian : 2.84% (population share)
           0%  (fatal encounter share)
           
   Hispanic : 4.94% (population share)
              22.7%  (fatal encounter share)


   ### Not sure where to start? ###
   - Try reading in either file and printing it to the screen 

   ### Note: You may use whatever functions you want.
   # For your reference, I've included headers for the functions I used

'''


def get_state_demographics(filename):
    '''
    Parameters: filename (string), name of the state demographic file
    Returns: state_list (list of strings), list of states in data
             demographics (list of lists of strings),
                 demographics[i] returns a list of a states demographics 
             demographic_order (list of strings),
                 order of groups in each demographics sublist

    Does: Reads a file of state demographic info
    '''


def get_fatal_encounter_data(filename):
    '''
    Parameters: filename (string), name of the fatal encounter datafile
    Returns: names, dates, ages, genders, races, record_states
             (all lists of strings)

    Does: Reads a file recording fatal police encounters
    '''
   

def print_names(names):
    '''
    Parameters: names (list of strings)
    Returns: none (Prints names, but no return value)

    Does: Prints every name in a list
    '''
   

def get_gender(genders):
    '''
    Parameters: genders (list of strings)
    Returns: none (Prints to screen, but no return value)

    Does: Prints the percent of males ('M') in the list
    '''
  
    

def get_ages(ages):
    '''
    Parameters: ages (list of strings)
    Returns: none (Prints to screen, but no return value)

    Does: Prints the youngest, oldest, and average age in the list
          NOTE: missing values (recorded as '') need to be removed
    '''
   

def get_state_info(state, state_list, demographics, demographic_order, \
                   races, record_states):
    '''
    Parameters: state (string), the state to report for
                state_list (list of strings), demographic state list 
                demographics (list of list of strings)
                demographic_order (list of strings)
                races (list of strings), race column from encounter data
                record_states (list strings), state column from encounter data
    Returns: none (Prints to screen, but no return value)

    Does: Prints a report for given state
          for each race/ethnicity
          list population share and fatality share
          
    '''
   

def main():

main()

'''
############ Put your answers here ###########

(1a) Print the name every person killed in a police encounter
     to your screen. (No output needed here)
(1b) How many people are listed in this dataset? 
(2) What percentage of fatalities were male?
(3) What is youngest, oldest, and average age in the dataset?
(4) For THREE states of your choosing, calculate:
    (a) the population share for each demographic category
    (b) the fatality share for each demographic category

'''
