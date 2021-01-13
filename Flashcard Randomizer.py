# Import the necessary packages
import pandas as pd
import random

# Read in the excel file containing the flashcards
df = pd.read_excel('./data/GRE Vocab List.xlsm', sheet_name = 'Master List')

# Pick a random flashcard out of all available flashcards in the deck
random = random.randint(0,df.shape[0])

# Tell the user the card the randomizer drew
print("YOUR WORD IS: " + df.iloc[random,0])
print("_____________________________________________________________________________________________________________ \n")

# Create a variable to hold a value that the upcoming loop will use as a check
booly = "True"

# Create a while loop that will ask the user for input and check for appropriate responses
while booly != "False":
    
    # Ask for the user's input regarding if they want to see the answer
    definition = input("""Type 'yes' or 'y' when you want to see the answer.
                   
Your response: """)
    print("_____________________________________________________________________________________________________________ \n")
 
    # If the user responds with an appropriate response, print both 'sides' of the flashcard
    if definition.lower() == 'yes' or definition.lower() == 'y':
        print("YOUR WORD WAS:     " + df.iloc[random, 0])
        print("THE DEFINITION IS: " + df.iloc[random, 1])
        booly = "False"
    
    # If the user does NOT respond with an appropriate response, prompt them to try inputting another response
    else:
        print("Your response is invalid. Try again. \n")
        print("_____________________________________________________________________________________________________________ \n")
