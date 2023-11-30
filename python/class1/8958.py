for _ in range(int(input())):
    s = input()
    sum = 0
    i=0
    for ox in s:
        if ox == "O":
            i+=1
            sum+=i
        else:
            i=0
    print(sum)