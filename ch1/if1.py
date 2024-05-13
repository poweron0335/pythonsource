# %%
if True:
    print("True")
# %%
a = 200
# a 가 100 보다 크고 200 보다 작거나 같냐
if a > 100 and a <= 200:
    print("a는 100보다 크고 200보다 작거나 같다")

# %%
if 100 < a <= 200:
    print("a는 100보다 크고 200보다 작거나 같다")

# %%
# 세 개의 숫자 중 가장 큰 수 출력
a, b, c = 12, 6, 18

max = a
if max < b:
    max = b
if max < c:
    max = c

print("a,b,c 중 가장 큰 수는 {}".format(max))

# %%
if True:
    print("True")
else:
    print("False")

# %%
score, grade = 90, "A"
# score 가 90 이상이고 grade 가 A => 합격
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

# %%
# 숫자를 입력 받은 후 짝/홀 출력
msg = int(input("숫자 입력"))
if msg % 2 == 0:
    print("짝수")
else:
    print("홀수")

# %%
# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50 보다 작다")
# %%
# 다중 if ==> switch(X)
# elseif(x) ==> elif
num = 90
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")

# %%
# age, height 입력받은 후
# age 가 20이상이고 height > 170 이상 : A 지망 지원 가능 출력
# age 가 20이상이고 height > 160 이상 : B 지망 지원 가능 출력
# age 가 20이상인데 height > 160 미만 : 지원 불가능 출력
# age 가 20미만 : 20세 이상 지원 가능
msg = int(input("age 입력"))
msg2 = int(input("height 입력"))

if msg >= 20 and msg2 >= 170:
    print("A 지망 지원 가능")
elif msg >= 20 and msg2 >= 160:
    print("B 지망 지원 가능")
elif msg >= 20 and msg2 < 160:
    print("지원불가")
else:
    print("20세 이상 지원 가능")

# %%
# 점수 입력 받ㅇ느 후
# 81 ~ 100 : A학점
# 61 ~ 80 : B학점
# 41 ~ 60 : C학점
# 21 ~ 40 : D학점
# 0 ~ 20 : E학점
num = int(input("점수 입력"))

if num >= 81:
    print("A학점")
elif num >= 61 and num <= 80:
    print("B학점")
elif num >= 41 and num <= 60:
    print("C학점")
elif num >= 21 and num <= 40:
    print("D학점")
else:
    print("E학점")
# %%
# 두개의 숫자 입력받기, 연산자(+, -, *, /, //, **, %) 입력받기
# 연산 후 결과 출력 (출력 예시 5 + 3 = 8)
num = int(input("숫자 입력"))
op = input("+, -, *, /, //, **, % 중 하나의 연산자 입력")
num2 = int(input("숫자 입력"))

result = None
if op == "+":
    result = num + num2
elif op == "-":
    result = num - num2
elif op == "*":
    result = num * num2
elif op == "/":
    result = num / num2
elif op == "//":
    result = num // num2
elif op == "**":
    result = num**num2
elif op == "%":
    result = num % num2


print("{} {} {} = {}".format(num, op, num2, result))
# %%
