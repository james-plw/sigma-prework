import random


def display_hangman(tries):  # ASCII art for each hangman stage, allows for 7 lives
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return HANGMANPICS[tries]


# word bank of just animals to make guessing simpler
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


def hangman_game():
    word = random.choice(words)  # chooses random word from list
    letters = list(word)  # turns word into list of letters

    progress = []  # for visual display of word length + correctly guessed letters
    for i in range(0, len(word)):
        progress.append("_")
    print(*progress)

    used_letters = []
    incorrect_guesses = -1
    while "_" in progress and incorrect_guesses < 6:
        correct = False
        letter = input("choose a letter: ")
        if letter not in used_letters:
            used_letters.append(letter)
        else:
            print("already picked that letter!")
            continue

        for i in range(0, len(word)):
            if letters[i] == letter:  # searching word for guessed letter
                progress[i] = letter  # adding correct letter to right spot
                correct = True  # establishing guess was correct

        if correct:
            print(*progress)
        else:
            incorrect_guesses += 1
            print(display_hangman(incorrect_guesses))

    if "_" not in progress:
        print("congratulations, the word was {}".format(word))
    elif incorrect_guesses == 6:
        print("you lost")
    else:
        print("situation not coded for")


while True:
    hangman_game()  # runs game

    while True:  # until user input is valid
        choice = input("That was fun, would you like to play again? (y/n) ")
        if choice in ('y', 'n'):
            break
        print('invalid input.')

    if choice == 'y':
        continue  # restarts game
    else:
        print('Okay goodbye!')
        break  # stops program
