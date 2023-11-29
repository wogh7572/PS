ex = [1, 2, 3, 4, 5, 6, 7, 8]
li = list(map(int, input().split()))
if li==ex:
    print('ascending')
elif li==ex[::-1]:
    print('descending')
else:
    print('mixed')