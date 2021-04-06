n = int(input())

first = n % 10
last = n // 100
second = n // 10 - (last * 10)
print(first + second + last)