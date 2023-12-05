def h_top(n, start, end):
    if n==1:
        print(start, end)
        return


    temp = 6-(start+end)
    h_top(n-1, start, temp)
    print(start, end)
    h_top(n-1, temp, end)

n = int(input())

print(2**n-1)
h_top(n, 1, 3)