# '#'과 '#' 바로 앞의 문자를 제거하는 함수 정의
def remove_hash_and_preceding_character(s):
    i = 0
    while i < len(s):
        # 현재 문자가 '#'인 경우
        if s[i] == '#':
            # i가 0보다 크면 (문자열 맨 앞이 아니라면)
            if i > 0:
                # '#' 바로 앞의 문자와 '#' 자체를 제거하고 문자열을 다시 조합
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                # 문자열의 맨 앞에 '#'이 있으면 '#' 자체만 제거
                s = s[i+1:]
        else:
            # '#'이 아닌 문자인 경우 인덱스 증가
            i += 1
    # 최종적으로 수정된 문자열 반환
    return s

# 두 문자열을 비교하여 '#'과 '#' 바로 앞의 문자를 제거하고 결과를 출력하는 함수 정의
def compareStrings(s1, s2):
    s1 = remove_hash_and_preceding_character(s1)
    s2 = remove_hash_and_preceding_character(s2)
    print(s1, s2)

    # 두 문자열이 동일한지 비교하고 결과 반환
    if s1 == s2:
        return 1
    else:
        return 0

# 예제 테스트
s1 = 'r#a#n#k#'
s2 = '###'
result = compareStrings(s1, s2)

# 결과 출력
print(result)  # 출력 결과: 1
