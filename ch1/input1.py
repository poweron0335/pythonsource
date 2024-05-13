# %%
print("Hello")

# %%
# input() : 사용자 입력을 받는 함수
msg = input()
print(msg)

# %%
msg = input("이름입력 : ")
print(msg)
# %%
msg = input("숫자 입력")
print(type(msg))
print(msg)
# %%
# 숫자 2개 입력받은 후 덧셈 결과 출력
msg = int(input("숫자 입력"))
msg2 = int(input("숫자 입력"))
result = msg + msg2
print("덧셈 결과 %d" % result)
# %%
