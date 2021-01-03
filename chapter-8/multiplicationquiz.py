# Project "Multiplication Quiz" given in chapter 8
# Code was given in the book itself. Had to modify the code to work without the importing of the pyinputplus module and implementing the following
# If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
# The user gets three tries to enter the correct answer before the program moves on to the next question.
# Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.
# Couldn't implement the 8 second delay without the module
# By Jithin John

import random, time

numberOfQuestions = 10
correctAnswers = 0
i=0

for questionNumber in range(numberOfQuestions):
    #Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    prompt = '#%s: %s x %s = '%(questionNumber+1, num1, num2)
    print(prompt)
    
    for i in range(3):
        #Right answers are handled by allowRegexes.
        #Wrong answers are handled by blockRegexes, with a custom message.
        testans = input()
        if testans == str(num1*num2):
        #This block runs if no exceptions were raised in the try block.
            print('Correct!')
            correctAnswers += 1
            time.sleep(1) #Brief pause to let user see the result
            break
        else:
            print('Incorrect')
            print(prompt)
    
print('Score: %s/ %s' %(correctAnswers, numberOfQuestions))