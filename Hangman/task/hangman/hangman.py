import random
import string

# initialisation of parameters
words_list = ["python", "java", "kotlin", "javascript"]
play = "play"

print("H A N G M A N")
while play == "play":
    selected_word = random.choice(words_list)
    word_set = set(selected_word)
    word_list = list(selected_word)
    lives = 8
    input_letters_set = set()

    # masking the randomly selected word
    i = 0
    while i < len(selected_word):
        word_list[i] = "-"
        i = i + 1
    new_word = "".join(word_list)
    new_word_list = list(new_word)
    new_word_set = set(new_word)

    # playing the game
    # cheking every letter against the randomly selected word
    play = str(input('Type "play" to play the game, "exit" to quit:'))
    while play == "play" and lives > 0 and word_set != new_word_set:
        print()
        print(new_word)
        input_letter = str(input("Input a letter:"))
        if len(input_letter) != 1:
            print("You should input a single letter")
        elif input_letter in string.ascii_lowercase:
            if input_letter in input_letters_set:
                print("You've already guessed this letter")
            elif input_letter in word_set and input_letter not in new_word_set:
                input_letters_set.add(input_letter)
                for j, char in enumerate(selected_word):
                    if char == input_letter:
                        new_word_list[j] = input_letter
                        new_word = "".join(new_word_list)
                        new_word_set = set(new_word)
            else:
                input_letters_set.add(input_letter)
                print("That letter doesn't appear in the word")
                lives -= 1
        else:
            print("Please enter a lowercase English letter")

    # printing the result
    else:
        if play == "play" and lives > 0:
            print(new_word)
            print("You guessed the word!")
            print("You survived!")
            print()
        elif play == "play":
            print("You lost!")
            print()
