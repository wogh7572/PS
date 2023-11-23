 for _ in range(int(input())):
    h, w, n = map(int, input().split())
    room = (n-1)//h+1
    floor = n%h
    result = floor*100 + room
    print(result)