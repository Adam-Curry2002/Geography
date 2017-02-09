import random
my_dict =   {
                "How many Vvlcanoes are int he RIng of Fire" : "452",
            }

#welcome message
print("Geography Revision Quiz")
print("=======================")

#the quiz will end when this variable becomes 'False'
playing = True

#While the game is running
while playing == True:

    #set the score to 0
    score = 0

    #gets the number of questions the player wants to answer
    num = int(input("\nHow many questions would you like: "))

    #loop the correct number of times
    for i in range(num):

        #the question is one of the dictionary keys, picked at random
        question = (random.choice( list(my_dict.keys())))
        #the answer is the string mapped to the question key
        answer = my_dict[question]



        #get the user's answer attempt
        guess = str(raw_input(("\nQuestion " + str(i+1)+(" ") )+(question  + "?")))

        #if their guess is the same as the answer
        if guess.lower() == answer.lower():
            #add 1 to the score and print a message
            print("Correct!")
            score += 1
        else:
            print("Nope! The correct answer was "+my_dict[question])

    #after the quiz, print their final score  
    print("\nYour final score was " + str(score))

    #store the user's input...
    again = raw_input("Enter any key to play again, or 'q' to quit.")

    #... and quit if they types 'q'
    if again.lower() == 'q':
        playing = False
