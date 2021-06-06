# put your python code here
list_numbers = []
result = 0
while len(list_numbers) < 1 or sum(list_numbers) != 0:
    list_numbers.append(int(input()))
if len(list_numbers) == 1:
    print(list_numbers[0])
else:
    for j in list_numbers:
        result += j**2
    print(result)
