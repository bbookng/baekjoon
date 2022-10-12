import sys
input = sys.stdin.readline

word1 = [''] + list(input().strip())
word2 = [''] + list(input().strip())

N, M = len(word1), len(word2)
cache = [[''] * M for _ in range(N)]

for i in range(1, N):
	for j in range(1, M):
			if word1[i] == word2[j]:
				cache[i][j] = cache[i-1][j-1] + word1[i]
			else:
				if len(cache[i-1][j]) >= len(cache[i][j-1]):
					cache[i][j] = cache[i-1][j]
				else:
					cache[i][j] = cache[i][j-1]

result = cache[-1][-1]

print(len(result))
print(result)