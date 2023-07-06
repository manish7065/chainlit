import random

def get_word_families(words, letter):
    word_families = {}
    for word in words:
        pattern = ''.join([letter if c == letter else '_' for c in word])
        if pattern in word_families:
            word_families[pattern].append(word)
        else:
            word_families[pattern] = [word]
    return word_families

def get_largest_word_family(word_families):
    largest_word_family = []
    for pattern, words in word_families.items():
        if len(words) > len(largest_word_family):
            largest_word_family = words
    return largest_word_family

def get_guess(word_families, guessed_letters):
    letter_frequencies = {}
    for pattern, words in word_families.items():
        for word in words:
            for letter in word:
                if letter not in guessed_letters:
                    if letter in letter_frequencies:
                        letter_frequencies[letter] += 1
                    else:
                        letter_frequencies[letter] = 1
    return max(letter_frequencies, key=letter_frequencies.get)

def play_hangman():
    with open('dictionary.txt') as f:
        words = [word.strip() for word in f.readlines()]
    word_length = int(input("Enter the length of the word: "))
    word_families = {'_' * word_length: words}
    guessed_letters = []
    lives = 6
    while lives > 0:
        print("You have", lives, "lives left.")
        pattern = max(word_families, key=lambda x: len(word_families[x]))
        print("Guess the word:", pattern)
        guess = get_guess(word_families, guessed_letters)
        print("Guessing letter:", guess)
        guessed_letters.append(guess)
        word_families = get_word_families(word_families[pattern], guess)
        if pattern == '_' * word_length:
            print("Congratulations! You guessed the word:", word_families[0])
            break
        largest_word_family = get_largest_word_family(word_families)
        if len(largest_word_family) == 1:
            print("Sorry, you ran out of lives. The word was", largest_word_family[0])
            break
        lives -= 1
    else:
        print("Sorry, you ran out of lives. The word was", random.choice(largest_word_family))

play_hangman()