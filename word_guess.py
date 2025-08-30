import random 

word_bank = ['rizz', 'skibidi', 'jamur','kenapa','jambu', 'siuuu']

word = random.choice(word_bank)

guessed_word = ['_'] * len(word)

attemps = 10

while attemps > 0 :
    print('\nCurrent Word: '+' '.join(guessed_word))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Great guess!')
    else:
        attemps -= 1
        print('Wrong guess! Attempts left: ' + str(attemps))

    if '_' not in guessed_word:
        print('\nCongratulations!! You Guessed the word: ' + word)
        break

if attemps == 0 and '_' in guessed_word:
    print('\nYou\'ve run out of attempts! The word was: ' + word)