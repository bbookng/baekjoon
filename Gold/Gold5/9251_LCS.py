import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

N, M = len(word1), len(word2)
cache = [0] * M

for i in range(N):
		cnt = 0
		for j in range(M):
				if cnt < cache[j]:
						cnt = cache[j]
				elif word1[i] == word2[j]:
						cache[j] = cnt + 1

print(max(cache))