#an attempt at making a hangman game in my last 3 days at adtran!
#QUESTIONS
    #categories? or just words???

#GLOBAL VARIABLE string of underscores / chars
word = ""
wordLength = 0

#GLOBAL VARIABLE CONST max amount of guesses (how many parts does mr hangman have)
allowedGuesses = 10 #head, body, arms, hands, legs, feet

#GLOBAL VARIABLE num of incorrect guesses
wrongGuesses = 0

#GLOBAL VARIABLE keep running game
continuePlaying = True

#display opening message function
def openingMessage:
    print "Hello! Welcome to Hangman. Preparing man to be hung...\nDone!\n\nPreparing word...\nDone!"
    
    print "Hope you're ready, here we go!"

#pick word function
def pickWord:

#generate array of underscores function
def generateString:

#play game function (wait for user input and bus it out somewhere else)
def playGame:
    pickWord
    while(continuePlaying):

        userInput = getInput
        inputValid = checkInput(userInput)

        if inputValid:
            correctInput
        else:
            incorrectInput

#get input from player
def getInput:

#check if input is in word
def checkInput:

#user gave correct input, update string
def correctInput:

#user gave last correct input, they win
def theyWin:
    continuePlaying = false

#user gave incorrect input, edit hangman and incorrect guesses
def incorrectInput:

#user maxed out guesses, they lose
def theyLose:
    continuePlaying = false


#play again?
def playAgain:

#dont need a main
