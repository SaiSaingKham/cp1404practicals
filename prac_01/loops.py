print("Odd numbers between 1 and 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print('\n')


print("Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print('\n')


print("Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print('\n')


n = int(input("Number of stars: "))
print("Print n stars:")
print('*' * n)
print()


print("Print n lines of increasing stars:")
for i in range(1, n + 1):
    print('*' * i)
