# %%
# while / for
# ++, -- (X)

i = 1
while i < 11:
    print(i)
    i = i + 1
# %%
# 1~100 사이의 짝수만 출력
i = 1
while i < 101:
    if i % 2 == 0:
        print(i, end=" ")
        i = i + 1
# %%
# 1~100 합계 구한 후 출력
i = 1
sum1 = 0
while i <= 100:
    sum1 += i
    i += 1
    print(sum1)

# %%
# 6단 구구단 출력
i = 1
while i < 10:
    print("%d x %d = %2d" % (6, i, (6 * i)))
    i += 1
# %%
# 사용자로부터 입력을 받은 후 화면 출력
# q 라는 문자 입력 시 입력 받는 것 중단
while True:
    str = input("입력")
    print(str)
    if str == "q":
        break
# %%
# for 변수명 in 범위:

range(5)
print(list(range(5)))  # 0 ~ 4
print(list(range(1, 5)))  # 1 ~ 4
print(list(range(1, 11, 2)))  # 1, 3, 5, 7, 9
# %%
i = 10
i
# %%
for i in range(1, 11):
    print(i, end=" ")
# %%
for i in range(1, 101, 2):
    print(i, end=" ")
# %%
# 1 ~ 100 합계 구하기
sum1 = 0
for i in range(1, 101):
    sum1 += i
sum1
# %%
# sum()
print(sum(range(1, 101)))
sum(range(1, 101, 2))
# %%
range(10, 1)
print(list(range(10, 1, -1)))
# %%
# 사용자로부터 숫자를 입력받은 후 1~ 사용자 입력 숫자까지 합계 구한 뒤 출력
num = int(input("숫자 입력"))

hap = 0
for i in range(1, num + 1):
    hap += i
print("1~{} 숫자 합 = {}".format(num, hap))
# %%
num = int(input("숫자 입력"))
print("1~{} 숫자 합 = {}".format(num, sum(range(1, num + 1))))

# %%
for s in "dreams":
    print(s, end=" ")

# %%
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# %%
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# %%
# 구구단 2~9단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, (i * j)), end= "\t")
    print()
# %%
# 리스트 ==> 자바, 자바스크립트 : 배열
numbers = [14, 3, 4, 5, 6, 7, 8, 33, 22, 55, 60]

for num in numbers:
    print(num)
# %%
# break

i = 1
while i < 11:
    if i == 5:
        break
    print(i, end=" ")
    i += 1
# %%
i = 1
while i < 11:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

# %%
