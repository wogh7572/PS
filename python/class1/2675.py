for _ in range(int(input())):
    num, s = list(map(str, input().split()))
    for i in s:
        print(i*int(num), end='')
    print()