import random


def display_hangman(tries):
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
                """,
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
                """,
              """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
                """,
              """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                -
                """,
              """
                --------
                |      |
                |      O
                |
                |
                |
                -
                """,
              """
                --------
                |      |
                |      
                |
                |
                |
                -
                """, ""
              ]
    return stages[tries]


print("Welcome to hangman")

word_list = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


word = get_word(word_list)

gamewin = False

guess = []

currword = []

tries = 7

goodguess = 0

while (gamewin == False):

    while True:
        letin = input("\nPlease enter a letter:")

        if len(letin) == 1 and letin.isalpha() and letin.lower() in guess:
            print("You have already guessed that letter")
        elif len(letin) == 1 and letin.isalpha():
            guess.append(letin.lower())
            break
        else:
            print("Please enter a valid, one character LETTER.")

    if letin.lower() in word.lower():
        print("\nCorrect guess.")
        goodguess += 1
    elif letin.lower() not in word.lower():
        print("\nIncorrect guess.")
        tries -= 1

    for letter in word:
        if letter.lower() in guess:
            print(letter, end=" ")
        elif letter.lower() not in guess:
            print("_", end=" ")
    print("")

    print(display_hangman(tries))

    print("Tries remaining: " + str(tries))

    if tries == 0:
        break
    elif goodguess == len(word):
        gamewin = True
        break

if gamewin == True:
    print("\nYou guessed the word in " + str(tries) + " tries", "\nThe word was: " + word)
else:
    print("\nYou were unable to guess the word.", "\nThe word was: " + word, "\nBetter luck next time.")