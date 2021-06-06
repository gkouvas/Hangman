vowels = set("aeiou")
word_list = list(input())
for char in word_list:
    if char in vowels:
        print("vowel")
    elif char.isalpha():
        print("consonant")
    else:
        break
