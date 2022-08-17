#UNIcompiler Internship Task-1
#This task is creating a number guessing game in which we have to guess a number in some given range and whenever our guess
#is wrong, we get another clue and the score gets reduced. The clue can be greater or less than, multiples, divisible, odd or
#even or combination of all.

import random as r
import math
print("**************   NUMBER GUESSING GAME  ***************")
print(""" *************       HELLO!!           ************
        ************ This is a number guessing game.  ************""")

print("************  5 Chances will be given to guess the number  **********")
print("************  If you are unable to guess the number in 5 guesses then you will lose the game.  *************")
print("************               Maximum score is 5         *************")
print("*********** Please enter the range in which you want to play the game  ***************")
print("****************************************************************************************")

x= int(input("Enter the lower bound of the range: "))
y= int(input("Enter the upper bound of the range: "))
random_number= r.randint(x,y)
guess= int(input("Enter the guessed number between {} and {}: ".format(x,y)))
max_score=5
if(guess==random_number):
    print("********* CONGRATULATIONS YOU WON THE GAME ************")
    print("*********    It is a correct guess!!  **************")
    print("********* Your final score is: " +str(max_score)+ " ***********")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

else:
    if(guess>random_number):
        print("This is greater than the number")
        print("Your score becomes: "+str(max_score-1))
        print("You have " +str(max_score-1)+ " guesses left now ")
        print("****************************************************")

    else:
        print("This is less than the number")
        print("Your score is: "+str(max_score-1))
        print("You have " +str(max_score-1)+ " guesses left now ")
        print("****************************************************")

    max_score=max_score-1 #4
    guess= int(input("Enter the new guess: "))
    if(guess==random_number):
        print("********* CONGRATULATIONS YOU WON THE GAME ************")
        print("*********    It is a correct guess!!  **************")
        print("********* Your final score is: " +str(max_score)+ "***********")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        
    else:
        if(random_number%2==0):
            print("It is an even number")
            print("Your score is: "+str(max_score-1))
            print("You have "+str(max_score-1)+ " guesses left now ")
            print("****************************************************")

        else:
            print("It is an odd number")
            print("Your score is: "+str(max_score-1))
            print("You have "+str(max_score-1)+ " guesses left now ")
            print("****************************************************")

        max_score=max_score-1 #3
        guess= int(input("Enter the new guess: "))
        if(guess==random_number):
            print("********* CONGRATULATIONS YOU WON THE GAME ************")
            print("*********    It is a correct guess!!  **************")
            print("********* Your final score is: "+str(max_score)+"***********")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        else:
            if(random_number%3 == 0):
                print("Number is divisible by 3")
                print("Your score is: "+str(max_score-1))
                print("You have "+str(max_score-1)+ " guesses left now ")
                print("****************************************************")

            else:
                for i in range(2,random_number+1):
                    if(random_number%i==0):
                        print("The number is multiple of "+str(i))
                        print("Your score is: "+str(max_score-1))
                        print("You have "+str(max_score-1)+ " guesses left now ")
                        print("****************************************************")

            max_score=max_score-1 #2 
            guess= int(input("Enter the new guess: "))
            if(guess==random_number):
                print("********* CONGRATULATIONS YOU WON THE GAME ************")
                print("*********    It is a correct guess!!  **************")
                print("********* Your final score is: "+str(max_score)+"***********")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

            else:
                for j in range(2,random_number):
                    if random_number%j == 0:
                        print("It is a composite number")
                    else:
                        print("It is a prime number")

                    max_score=max_score-1 #1
                    print("It is your last chance to guess the number otherwise you will lose the game")
                    guess= int(input("Enter the new guess: "))
                    if(guess==random_number):
                        print("********* CONGRATULATIONS YOU WON THE GAME ************")
                        print("*********    It is a correct guess!!  **************")
                        print("********* Your final score is: "+str(max_score)+"***********")
                        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    else:
                        print("***********  SORRY YOU LOST THE GAME  **************")
                        print("********* The number was: "+str(random_number)+" ************")
                        print("***********  Your final score is "+str(max_score-1)+" ************")
                        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
