#an attempt at making a hangman game in my last 3 days at adtran!
#QUESTIONS
    #categories? or just words???
    #irc?

#GLOBAL VARIABLE string of underscores / chars
word = ""
wordWorking = ""
wordLength = 0

#GLOBAL VARIABLE CONST max amount of guesses (how many parts does mr hangman have)
allowedWrongGuesses = 10 #head, body, arms, hands, legs, feet

#GLOBAL VARIABLE num of incorrect guesses
wrongGuesses = 0
rightGuesses = 0

#GLOBAL VARIABLE keep running game
continuePlaying = True

#display opening message function
def openingMessage():
    print "Hello! Welcome to Hangman. Preparing man to be hung...\nDone!\n\nPreparing word...\nDone!"
    
    print "Hope you're ready, here we go!\n\n"

#pick word function
def pickWord():

#generate array of underscores function
def generateString():

#play game function (wait for user input and bus it out somewhere else)
def playGame():
    pickWord
    while(continuePlaying):

        showGame
        userInput = input("Guess a letter: ")
        inputValid = checkInput(userInput)

        if inputValid:
            correctInput
        else:
            incorrectInput

    playAgain

#check if input is in word
def checkInput(userInput):

#show game board
def showGame():

#user gave correct input, update string
def correctInput(userInput):
    rightGuesses = rightGuesses + 1
    print "Right! :D Your guess " userInput " is in the word."

#user gave last correct input, they win
def theyWin():
    continuePlaying = false

#user gave incorrect input, edit hangman and incorrect guesses
def incorrectInput(userInput):
    wrongGuesses = wrongGuesses + 1
    print "Wrong >:( Your guess " userInput " is not in the word.\nMr. Hangman gets another body part."
    
    remaining = allowedWrongGuesses - wrongGuesses
    if(remaining <= 4):
        print "Warning!!! Only " remaining " wrong guesses remaining!"

#user maxed out guesses, they lose
def theyLose():
    continuePlaying = false


#play again?
def playAgain():
    play = input("Do you want to play again? (y/n): ")
    if (play == "y" || play == "Y"):
        print "Yay!! Here we go again!!!!!"
        playGame
    else:
        print "Baiiiii"


#dont need a main
openingMessage
playGame