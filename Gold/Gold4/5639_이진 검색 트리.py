import sys
sys.setrecursionlimit(10**9)

arr = []

while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

def postorder(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1, e+1):
        if arr[s] < arr[i]:
            mid = i
            break

    postorder(s+1, mid-1)
    postorder(mid, e)
    print(arr[s])


postorder(0, len(arr)-1)




