#an attempt at making a hangman game in my last 3 days at adtran!
#TODO: 
#   - QUESTIONS
#       - categories? or just words???
#       - irc?
#       - name the hangman?
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol, defer
import random
try:
    from builtins import input as raw_input
except ImportError:
    pass

class hangman(irc.IRCClient):
    serv_ip = 'coop.test.adtran.com'
    serv_port = 6667
    channel = '#test'
    owner = 'bmoussadcomp.adtran.com'
    nickname = 'hangman'

    #display opening message function
    def openingMessage(self):
        print("\n\nHello! Welcome to Hangman. Preparing man to be hung...\nDone!\n\nPreparing word...\nDone!")
        
        print("\nHope you're ready, here we go!\n\n")

    #pick word function
    def pickWord(self):
        global word
        global wordRemoving
        lines = open('words.txt').read().splitlines()
        myline =random.choice(lines)
        word = myline
        wordRemoving = word
    #generate array of underscores function
    def generateString(self):
        global wordWorking
        i = 1
        dash = "-"
        wordWorking = "-"
        while (i < len(word)):
            wordWorking = wordWorking + dash
            i = i + 1

    #play game function (wait for user input and bus it out somewhere else)
    def playGame(self):
        global continuePlaying
        global usedChars
        global wordRemoving
        global word
        global wordWorking
        global wrongGuesses 
        global wrongGuesses 
        global wrongGuesses 
        wrongGuesses = 0
        rightGuesses = 0
        wordRemoving = ""
        word = ""
        wordWorking = ""
        usedChars = ""
        self.pickWord()
        self.generateString()
        usedChars = ""
        while(self.continuePlaying):

            self.showGame()
            print("\nCharacters guessed: " + usedChars)
            userInput = input("Guess a letter: ")
            if (userInput in usedChars):
                print(userInput + " already guessed, go again\n")
                continue

            inputValid = checkInput(userInput)
            if(wrongGuesses == 0 and rightGuesses == 0):
                usedChars = userInput
            else:
                usedChars = usedChars + ", " + userInput


            if(inputValid and (rightGuesses < len(word))):
                correctInput(userInput)
            elif(inputValid and (rightGuesses == len(word))):
                self.theyWin()
            elif(not inputValid and (wrongGuesses <= allowedWrongGuesses)):
                incorrectInput(userInput)
            elif(not inputValid and (wrongGuesses > allowedWrongGuesses)):
                self.theyLose()

        self.playAgain()

    #check if input is in word
    def checkInput(self, userInput):
        return (userInput in self.wordRemoving)

    #show game board
    def showGame(self):
        if(wrongGuesses == 0):
            print(self.hangmanEmpty)
        elif(wrongGuesses == 1):
            print(hangman1)
        elif(wrongGuesses == 2):
            print(hangman2)
        elif(wrongGuesses == 3):
            print (hangman3)
        elif(wrongGuesses == 4):
            print (hangman4)
        elif(wrongGuesses == 5):
            print (hangman5)
        elif(wrongGuesses == 6):
            print (hangman6)
        elif(wrongGuesses == 7):
            print (hangman7)
        elif(wrongGuesses == 8):
            print (hangman8)
        elif(wrongGuesses == 9):
            print (hangman9)
        elif(wrongGuesses == 10):
            print (hangman10)
        
        print(wordWorking)
        

    #user gave correct input, update string
    def correctInput(self, userInput):
        global rightGuesses
        global wordRemoving
        global wordWorking
        rightGuesses = rightGuesses + 1
        print ("Right! :D Your guess " + userInput + " is in the word.\n")

        while(userInput in wordRemoving):
            index = wordRemoving.find(userInput)
            l1 = list(wordRemoving)
            l1[index] = '*'
            wordRemoving = "".join(l1)

            l2 = list(wordWorking)
            l2[index] = userInput
            wordWorking = "".join(l2)
        
        if(wordWorking == word):
            self.theyWin()


    #user gave last correct input, they win
    def theyWin(self):
        global continuePlaying
        continuePlaying = False
        print("`~`~` Congrats!!!! You got the winning word: " + word + "!!!!`~`~`")

    #user gave incorrect input, edit hangman and incorrect guesses
    def incorrectInput(self, userInput):
        global wrongGuesses
        remaining = allowedWrongGuesses - wrongGuesses
        wrongGuesses = wrongGuesses + 1
        if(remaining > 0):
            print ("Wrong >:( Your guess " + userInput + " is not in the word.\nMr. Hangman gets another body part.\n")
            if(remaining <= 4):
                print ("Warning!!! Only " + str(remaining) + " wrong guesses remaining!")
        else:
            self.theyLose()
        

    #user maxed out guesses, they lose
    def theyLose(self):
        global continuePlaying
        continuePlaying = False
        print("\n\nboi you dun goofed and hangman is ded. Winning word was: " + word)


    #play again?
    def playAgain(self):
        global continuePlaying
        play = raw_input("Do you want to play again? (y/n): ")
        if (play == "y" or play == "Y"):
            print ("Yay!! Here we go again!!!!!")
            continuePlaying = True
            self.playGame()
        else:
            print ("Baiiiii")


    #dont need a main 
#dont need a main
    #dont need a main 
    # TODO:
    #      -;-; i wish you had
    #GLOBAL VARIABLE string of underscores / chars
    wordRemoving = ""
    word = ""
    wordWorking = ""
    wordLength = 0
    usedChars = ""
    hangmanEmpty = "   ____\n  |    |\n  |\n  |\n  |\n  |\n__|__"
    hangman1 = "   ____\n  |    |\n  |   ( )\n  |\n  |\n  |\n__|__"
    hangman2 = "   ____\n  |    |\n  |   ( )\n  |    |\n  |\n  |\n__|__"
    hangman3 = "   ____\n  |    |\n  |   ( )\n  |   \|\n  |\n  |\n__|__"
    hangman4 = "   ____\n  |    |\n  |   ( )\n  |  '\|\n  |\n  |\n__|__"
    hangman5 = "   ____\n  |    |\n  |   ( )\n  |  '\|/\n  |\n  |\n__|__"
    hangman6 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |\n  |\n__|__"
    hangman7 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |   /\n  |\n__|__"
    hangman8 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |  _/\n  |\n__|__"
    hangman9 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |  _/ \\\n  |\n__|__"
    hangman10 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |  _/ \\_\n  |\n__|__"

    #GLOBAL VARIABLE CONST max amount of guesses (how many parts does mr hangman have)
    allowedWrongGuesses = 10 #head, body, arms, hands, legs, feet

    #GLOBAL VARIABLE num of incorrect guesses
    wrongGuesses = 0
    rightGuesses = 0

    #GLOBAL VARIABLE keep running game
    continuePlaying = True
    def main(self):
        f = protocol.ReconnectingClientFactory()
        f.protocol = hangman
        reactor.connectTCP(self.serv_ip, self.serv_port, f)
        reactor.run()
       

if __name__ == '__main__':
    bot = hangman()
    bot.main()