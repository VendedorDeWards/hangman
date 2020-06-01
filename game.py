####################################
########    NEEDS ERROR    #########
########      HANDLING     #########
####################################

import ast, os, random

def game_start():
    global max_attempts
    global errors
    global guesses
    global word
    global game_word
#    global min_length
    max_attempts = 0
    errors = 0
    guesses = []
    game_word = []

    os.system('cls')
    
    print('Starting a game of Hangman: Films...')
    while not (max_attempts := input('How many incorrect attempts you want? [1-10]... ')).isnumeric() or not int(max_attempts) <= 10 or not int(max_attempts) >= 1:
        print("%s is not an integer between 1 and 10" %max_attempts)
    max_attempts = int(max_attempts)
#    while not (min_length := input('What minimum word length do you want? [4-16]... ')).isnumeric or not int(min_length) <= 16 or not int(min_length) >= 4:
#        print("%s is not an integer between 4 and 16" %min_length)
#    min_length = int(min_length)
    print('Selecting a film...')
    #    word selection takes place!
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'films.txt')
    with open(my_file, 'r') as f:
        words = ast.literal_eval(f.read())
        word = words[random.randint(0, len(words)-1)].lower()
    for i in range(len(word)):
        if word[i] == ' ':
            game_word.append(' ')
        else:
            game_word.append('_')
    print()

def game_turn():
    global max_attempts
    global errors
    global guesses
    global word
    global game_word
    print('Film: ' + " ".join(game_word))
    print('Attempts remaining: ' + str(max_attempts - errors))
    print('Previous Guesses: ' + " ".join(guesses))
    while (letter := input('Choose the next letter... ')) in guesses or not letter.isalpha() or len(letter) != 1:
        if letter in guesses:
            print('%s has already been guessed before' %letter)
        if not letter.isalpha() or len(letter) != 1:
            print('Input must be a valid letter')
    
    os.system('cls')
    
    guesses.append(letter)
    if letter in list(word):
        print("%s IS in the film!" %letter)
        for let in range(len(word)):
            if letter == word[let]:
                game_word[let] = letter
    else:
        print("%s IS NOT in the film!" %letter)
        errors += 1

max_attempts = 0
errors = 0
guesses = []
#min_length = 0
word = ''
game_word = []

game_start()
while True:
    if all(letter.isalpha() or letter.isspace() for letter in game_word):
        print('Game Finished, You Won!')
        print('Film was: %s' %word)
        while not (play_again := input('Do you want to play again? [y-n]...')) in ['y', 'n']:
            print('Input must be y for yes or n for no')
        if play_again == 'y':
            game_start()
            continue
        else:    
            break
    game_turn()
    if errors == max_attempts:
        print('Game Finished, You Lost!')
        print('Film was: %s' %word)
        while not (play_again := input('Do you want to play again? [y-n]...')) in ['y', 'n']:
            print('Input must be y for yes or n for no')
        if play_again == 'y':
            game_start()
            continue
        else:    
            break
exit()