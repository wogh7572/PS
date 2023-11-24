arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
max_n=0
max_li=[]
arr.sort()
arr1 = sorted(list(set(arr)))
for i in arr1:
    if arr.count(i)>max_n:
        max_n = arr.count(i)
        max_li = [i]
    elif arr.count(i)==max_n:
        max_li.append(i)
    

arr_sum = sum(arr)
print(arr)
#산술
print(round(arr_sum/n, 0))
#중앙값
print(arr[n//2])
#최빈값
if len(max_li)==1:
    print(max_li[0])
else:
    print(max_li[1])
#범위
print(max(arr)-min(arr))
print()
print(max_li)

