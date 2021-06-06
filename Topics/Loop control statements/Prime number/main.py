number = int(input())
i = 2
result = "This number is prime"
if number > 1:
    for i in range(i, number):
        if number % i == 0:
            result = "This number is not prime"
else:
    result = "This number is not prime"
print(result)
