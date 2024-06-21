import random 

print("HANGMAN")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


games = ["cricket", "football", "kabadi", "hockey", "kho-kho", "tennise", 
          "free fire", "bgmi", "chess", "carrom", "table tennise"]

fruit = random.choice(games)

chances = len(games)+2

stage = 6

guesses = ""

while(chances > 0):

    loss = 0

    for i in fruit:
        if i in guesses:
            print(i,end="")
        else:
            print("_",end="")
            loss += 1

    print()

    if loss == 0:
        print("YOU WON THIS MATCH!!")
        break

    guess = input("Enter the character: ")
    guesses += guess

    if guess not in games:
        chances -= 1
        print(stages[stage])
        stage -= 1

    if chances == 0:
        print("You have lost all your chances")
