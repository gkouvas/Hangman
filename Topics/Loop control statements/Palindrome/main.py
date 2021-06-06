input_word = str(input())
input_list = list(input_word)
n = len(input_word) / 2
i = 0

while (input_list[i] == input_list[-(i + 1)]) and (i < n):
    i += 1
if i == n:
    print("Palindrome")
else:
    print("Not palindrome")
