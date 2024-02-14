
def solution(s, word_dict):
    max_answer = [0]
    def bt(s, i, cnt):

        if i == len(s)-1:
            if max_answer[0] < cnt:
                max_answer[0] = cnt
            return

        for word_index in range(len(word_dict)):
            if s[i:i+len(word_dict[word_index])] == word_dict[word_index]:
                bt(s, i+len(word_dict[word_index])-1, cnt+1)

    bt(s, 0, 0)
    return max_answer[0]

print(solution("centerminus", ["cent", "center", "term", "terminus", "rm", "min", "minus", "us"]))
print(solution("aaaababab", ["aaa", "aaaa", "ab", "bab", "aababa"]))

