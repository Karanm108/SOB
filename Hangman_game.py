## In this code i have made a hangman game where the user has 6 attempts to guess the word if failed the game will be over and the user would be asked if they want to play again.
import random


## Pictures for the hamgman game in a list
HANGMAN_PICS = ["""         
 +===+
     |
     |
     |
    ===
""", """
 +===+
 O   |
     |
     |
    ===
""", """
 +===+
 O   |
 |   |
     |
    ===
""", """
 +===+
 O   |
/|   |
     |
    ===
""", """
 +===+
 O   |
/|\  |
     |
    ===
""", """
 +===+
 O   |
/|\  |
/    |
    ===
""", """
 +===+
 O   |
/|\  |
/ \  |
    ===
"""]

words = ["rhino", "porsche", "quill", "haemoglobin", "hello"] ##list of words that the user has to guess from

def getRandomWord(wordList):    ##functions for getting a random wornd from the list 
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]
    

def displayBoard(missedLetters, correctLetters, secretWord, hangman_pics):  ##function to display the the hangman what correct they selected the letters they got wrong and will display the secrert word when they win or lose
    print(hangman_pics[len(missedLetters)])
    print("\n")
    print(f"Missed letters: {missedLetters}")
    print("\n")

    blanks = ''

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks + secretWord[i]
        else:
            blanks = blanks + '_'

    for character in blanks:
        print(character + ' ', end = '')
    print("\n")
          

def getGuess(alreadyGuessed): ## this function is for when a player inputs a letter they alredy guessed or is they enter a word or anything else it will tell them to enter a single letter 
    
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()

        if guess in alreadyGuessed:
            print("You have already guessed this letter.")

        elif len(guess) != 1:
            print("Please enter a single letter...")

        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter...")
        
        else:
            return guess

def playAgain(): ##this function will ask the player if they want to play again if y a new word will be selected and if n the code will break
    print("Do you wanna play again? | y/n")

    response = input()
    response.lower()

    while response != 'y' and response != 'n':
        print("Do you wanna play again? | y/n")

        response = input()
        response.lower()

    if response == 'y':
        return True
    elif response == 'n':
        return False

    

##################### MAIN #######################

print("H A N G M A N")

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)

gameIsDone = False

while True: ## this loop will run until the player guessed the word corectly or has run out of turns and wishes to quite or continue again
    displayBoard(missedLetters, correctLetters, secretWord, HANGMAN_PICS)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False

        if foundAllLetters == True:
            print("Yes! The secret word is " +secretWord + ". You have won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord, HANGMAN_PICS)
            print("You've run out of guesses!")
            print(f"The word was {secretWord}")
            gameIsDone = True

        


    if gameIsDone == True:

        if playAgain() == True:
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)

            gameIsDone = False
            
        else:
            break





























