import sys


from collections import Counter


n = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for i in range(n)])



cnt = Counter(arr).most_common()

print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])




if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])


print(max(arr)-min(arr))