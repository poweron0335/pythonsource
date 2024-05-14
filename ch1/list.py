# %%
# 숫자, 문자열

# 데이터 모임 표현 : list(== ArrayList(배열)), dict(== Map), set(== HashSet), tuple()
# 동일한 타입만을 담지 않음
# %%
# 리스트 생성
list1 = []
list2 = [1, 2, 3, 4, 5, 6]
list3 = [1, "a", 3, "b", 5, 6]
list4 = [1, 2, 3, 4, 5.5, 6.5]
list5 = [1, 2, 3, 4, ["Life", "is", "short"]]
list6 = list([3, 4, 5])

# %%
# 출력
print(list2)
# %%
# 리스트 인덱싱 / 슬라이싱
print(list2[2])
print(list3[-2])
print(list4[-1])
print(list5[-1])
print(list5[4])
print(list5[4][0])
print(list5[4][2])

# %%
list7 = [1, 2, 3, 4, ["a", "b", ["Life", "is"]]]
print(list7[4][2][1])
print(list7[-1][2][1])
print(list7[-1][-1][-1])
# %%
print(list2)
print(list2[2:4])
print(list2[:4])
print(list2[:-1])
# %%
print(list5)
print(list5[4:])
print(list5[4][:2])
# %%
# list 연산자
# + : 연결 연산자
print(list2 + list3)
print(list5 + list6)
print(list2[1] + list3[0])  # 요소와 요소일 때는 산술 개념으로 사용
# %%
# * : 반복
print(list2 * 2)
# %%
# len() : 길이
len(list2)
# %%
# 리스트 수정 / 삭제
list2[0] = 7
print(list2)

list2[1] = [10, 11, 12]
print(list2)

del list2[1]
print(list2)

del list2[2:]
print(list2)
# %%

for i in list3:
    print(i, end="\t")
# %%
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 100 이상의 요소만 출력
for i in numbers:
    if i >= 100:
        print(i)

# %%
# 홀수, 짝수 구분하여 출력
for i in numbers:
    if i % 2 == 0:
        print("{}는 짝수".format(i))
    else:
        print("{}는 홀수".format(i))
# %%
# 숫자의 자릿수 출력
for i in numbers:
    print("{} : {}".format(i, len(str(i))))
# %%
# list 함수
# 1) append() : 리스트에 요소 추가하기
list3.append(["c", "d", "e"])
print(list3)
list3.append(5)
print(list3)
# %%
# 1~100 까지 숫자 중에서 짝수만 리스트로 생성
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
print(even)
# %%
# 2) sort() : 오름차순 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ["a", "e", "g", "b", "c"]
a.sort()
print(a)

a = ["ㅎ", "ㄱ", "ㅈ", "ㅁ", "ㅋ"]
a.sort()
print(a)

# %%
# 3) reverse() : 리스트 뒤집기(역순 정렬 x)
print(list4)
list4.reverse()
print(list4)
# %%
# 4) index() : 인덱스 값 리턴

list4.index(3)
list4.index(6)
# %%
# 5) remove() == del 요소지정
# 처음 만나는 요소 제거

# list4.remove()
# print(list4)
list4.append(5.5)
print(list4)

list4.remove(5.5)
print(list4)

# %%
# 6) pop() : 맨 마지막 리스트 요소 꺼내기
list4.pop()
list4

# %%
# pop(인덱스) : 인덱스 요소 꺼내기(==제거)
list4.pop(1)
list4
# %%
# 7) count(찾을 요소) : 찾을 요소 개수 리턴
list4 = [12, 13, 14, 15, 14]
list4.count(14)
# %%
# 8) extend() : + 같은 역할
list4.extend([16, 17, 18])
list4

# %%
# 9) clear() : 리스트 요소 모두 삭제
list4.clear()
list4
# %%
numbers
# %%
numbers.sort(reverse=True)
# %%
numbers
# %%
# 거짓에 해당 : "", [], (), {}, 0
city = ""
list8 = []

if city:
    print("비어 있지 않음")
else:
    print("비어 있음")

if list8:
    print("비어 있지 않음")
else:
    print("비어 있음")
# %%
fruits = ["딸기", "바나나", "사과", "배", "수박"]

# in == sql in 연산자와 동일 개념
if "딸기" in fruits:
    print("딸기 요소가 포함됨")

print("메론" not in fruits)
# %%
a_class = [70, 60, 55, 75, 92, 80, 85, 100, 87, 65]

# a_class 평균과 총합을 구하시오

sum1 = 0
for i in a_class:
    sum1 += i
print(f"총합 : {sum1}, 평균 : {sum1/len(a_class)}")

# %%
# sum()
print(f"총합 : {sum(a_class)}, 평균 : {sum(a_class)/len(a_class)}")

# %%
# 리스트 컴프리헨션(comprehension)

numbers = []

# 요소 추가
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.append(7)

numbers
# %%
numbers = []
for i in range(1, 101):
    numbers.append(i)

numbers

# %%
numbers = list(range(1, 101))
numbers
# %%
numbers = [x for x in range(1, 101)]
numbers
# %%
a = [1, 2, 3, 4]
# a 라는 리스트 요소에 *3을 한 후 결과를 새로운 리스트로 돌려받기
result = []
for i in a:
    result.append(i * 3)

result
# %%
result2 = [i * 3 for i in a]
result2
# %%
b = ["갑", "을", "병", "정"]
# b 라는 리스트에서 정 요소를 제외하고 새로운 리스트로 돌려받기

result = []
for i in b:
    if i != "정":
        result.append(i)
result
# %%
result2 = [i for i in b if i != "정"]
result2
# %%
a = [1, 2, 3, 4]
# 짝수에만 3을 곱해서 담고 싶다면 : [6,12]
result2 = [i * 3 for i in a if i % 2 == 0]
result2
# %%
# 1 ~ 100 숫자 중에서 홀수만 담아서 새로운 리스트로 생성
result = []
for i in list(range(1, 101)):
    if i % 2 == 1:
        result.append(i)
result

result2 = [i for i in range(1, 101) if i % 2 == 1]
result2
# %%
list1 = ["nice", "study", "python", "anaconda", "!"]
# 5글자 이상의 요소만 담아서 새로운 리스트로 생성
result = []
for i in list1:
    if len(i) >= 5:
        result.append(i)
result

result2 = [i for i in list1 if len(i) >= 5]
result2
# %%
list1 = ["A", "b", "c", "D", "e", "F", "G", "h"]
# 소문자만 담아서 새로운 리스트로 생성
result = []
for i in list1:
    if i == i.lower():
        result.append(i)
result

result2 = [i for i in list1 if i == i.lower()]
result2
# %%
# [1,2,3,4] ==> [2,4,6,8]
# [0,1,2,3,4] ==> [0,1,4,9,16]
list1 = [1, 2, 3, 4]
list2 = [0, 1, 2, 3, 4]
result = []
for i in list1:
    result.append(i * 2)
result

result2 = [i * 2 for i in list1]
result2

print([x * x for x in range(5)])
# %%
# [1,2,3]
# [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

print([[x, x + 1, x + 2] for x in [1, 2, 3]])
# %%
# 주차장 프로그램 작성
parking_lot = []
top, car_name = 0, "A"
while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :"))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print(f"{car_name} 자동차 들어감. 주차장 상태 ==> {parking_lot}")

                top += 1
                car_name = chr(ord(car_name) + 1)
        elif no == 2:
            if top > 0:
                outCar = parking_lot.pop()
                print(f"{outCar} 자동차 나감. 주차장 상태 ==> {parking_lot}")
                top -= 1
                car_name = chr(ord(car_name) - 1)
            else:
                print("빠져나갈 자동차가 없음")

        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요")
# %%
# ord() : 특정 문자열 유니코드 값 반환
# chr() : 유니코드 값 특정 문자열 반환
print(ord("A"))
print(chr(65))
# %%
# enumerate() : 리스트, 튜플, 문자열 값을 입력받아 인덱스 값을 포함하는 객체로 만들어 줌

list1 = ["body", "foo", "bar"]
for x in enumerate(list1):
    print(x)

for idx, value in enumerate(list1, start=1):
    print(idx, value)
# %%
