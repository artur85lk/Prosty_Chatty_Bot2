first = int(input())
second = int(input())
new_first = first * 1
new_second = second * 1
conter = 0
while new_first > new_second:
    new_first = new_first / 2
    conter = conter + 1
print(conter * 12)