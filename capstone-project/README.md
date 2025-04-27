For this project I created a hangman game, playable inside the command line.
The python code used to run the game contains ASCII art for 7 stages of hangman, allowing for 7 lives/incorrect guesses in the game, along with a word bank of animal names to narrow the range of possible words the player has to guess.
The random module is used to pick a random word, which the player then has to guess, one letter at a time until they run out of lives or guess the word correctly.
The main part of the game is contained within the hangman_game function, allowing it to be recalled if the player wishes to play again.

The code is all contained inside the [hangman.py file](https://github.com/james-plw/sigma-prework/blob/main/capstone-project/hangman.py).

To run the code, download the file using the link above and, when in the same directory in the command line, use 'python3 hangman.py'.
The command line will show a series of underscores '_' showing how long the word is.
Enter a lowercase letter at a time and don't worry about guessing the same letter again, as the game will tell you that you have, and it won't use up a life.
Once the game has finished you can play again by entering 'y' when prompted or 'n' if you are finished.
