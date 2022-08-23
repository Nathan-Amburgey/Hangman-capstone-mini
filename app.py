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

def lose6LifeState():
    print("--------")
    print(" |     |")
    print(" O     |")
    print("\|/    |")
    print("/ \    |")
    print("    ----")


lives = 6
running = True
while running:
    print("Hard Hangman")
    print("Press 'p' to start game")
    print("Press 'q' to quit")

    input = input("Enter command: ")
    if input == "q" or input == "Q":
        running = False
    else:
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
        else:
            lose5LifeState()
            print("You lose")
            running = False
            
            
        

       
