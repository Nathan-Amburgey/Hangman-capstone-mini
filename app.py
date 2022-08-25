import json
import requests
def startGameState():
    print("--------")
    print(" |     |")
    print("       |")
    print("       |")
    print("       |")
    print("    ----")

def lose1LifeState():
    print("--------")
    print(" |     |")
    print(" O     |")
    print("       |")
    print("       |")
    print("    ----")

def lose2lifeState():
    print("--------")
    print(" |     |")
    print(" O     |")
    print(" |     |")
    print("       |")
    print("    ----")

def lose3LifeState():
    print("--------")
    print(" |     |")
    print(" O     |")
    print("\|     |")
    print("       |")
    print("    ----")

def lose4LifeState():
    print("--------")
    print(" |     |")
    print(" O     |")
    print("\|/    |")
    print("       |")
    print("    ----")

def lose5LifeState():
    print("--------")
    print(" |     |")
    print(" O     |")
    print("\|/    |")
    print("/      |")
    print("    ----")
    print("Hint: pronounced " + jdata[0]['pronunciation'])

def lose6LifeState():
    print("--------")
    print(" |     |")
    print(" O     |")
    print("\|/    |")
    print("/ \    |")
    print("    ----")

# Get letters user guessed
def getUserGuess(word, guessedIndices):
    guess = ""
    length = len(word)
    for i in range(length):
        if i in guessedIndices:
            guess += " " + word[i]
        else:
            guess += ' _'
    return guess

# Check if character in the word
def checkCharacterInWord(guess, word, guessedIndices):
    length = len(word)
    count = 0
    for i in range(length):
        if i not in guessedIndices and word[i] == guess:
            guessedIndices.add(i)
            count += 1
    
    return count > 0
            

lives = 6
running = True

print("Shitty Hangman")
startGameState()

# Fetch random word
rndWord = requests.get("https://random-words-api.vercel.app/word")
Apidata = rndWord.text
jdata = json.loads(rndWord.text)
word = jdata[0]['word']
word = word.lower()
guessedIndices = set()
guessedLetters = set()
userGuess = getUserGuess(word, guessedIndices)
print(userGuess)

while running:
    # Get user guess
    guess = input("Enter a letter to guess: ")
    guess = guess.lower()
    if guess not in guessedLetters:
        guessedLetters.add(guess)
    else:
        print("Letter already guessed")
        continue

    # Check if letter in word
    guessInWord = checkCharacterInWord(guess, word, guessedIndices)
    if not guessInWord:
        lives -= 1

    userGuess = getUserGuess(word, guessedIndices)

    # Print output
    if lives == 6:
        startGameState()
    elif lives == 5:
        lose1LifeState()
    elif lives == 4:
        lose2lifeState()
    elif lives == 3:
        lose3LifeState()
    elif lives == 2:
        lose4LifeState()
    elif lives == 1:
        lose5LifeState()
    elif lives == 0:
        lose6LifeState()
        print("The word was " + word)
        print("You lose")
        running = False
        continue

    print(userGuess)
    print("Guessed Letters: " + guessedLetters.__str__())
    # Check for win
    if "_" not in userGuess:
        print("You win!")
        running = False
        continue


            
        

       
