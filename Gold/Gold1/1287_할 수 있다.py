import sys
input = lambda :sys.stdin.readline().strip()

S=input()
try:
    eval(S.replace("+","&").replace("-","&").replace("/","&").replace("*","&"))
    print(int(eval(S.replace("/","//"))))
except:print("ROCK")