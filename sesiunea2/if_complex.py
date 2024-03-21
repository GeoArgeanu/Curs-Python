# 1. nested if
a, b, c = 3, 5, 7
if a > b:
    if c != 0:
        print('c diferit de o')
    else:
        print(c)
else:
    if c == 0:
        print('c este 0')

# conditii multiple
x, y, z = 0, 2, 4
# verificam daca toate nr sunt pare
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print('toate sunt pare')
elif x % 2 == 0 or z % 2 == 0:
    print('cel ptin unul este par')
else:
    print('toate sunt impare')

