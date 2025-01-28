### 2-1. 숫자형

# a=123
# a=-178
# a=0
# a=0o177
# print(a)
# a=0x8ff
# b=0xABC
# print(b)
# a=3
# b=4
# a+b
# a*b
# a/b
# a=3
# b=4
# print(a**b)
# print(7%3)
# print(3%7)
# print(7/4)
# print(7//4)

### 2-2. 자료형
# print("Hello World")
# print("Python is fun")
# print("""Life is too short, You need python""")
# print('''Life is too short, you need python''')
# print("Python's favorite food is perl")
# food="Python's favorite food is perl"
# print(food)
# food='Python\'s favorite food is perl'
# print(food)
# say="\"Python is very easy.\" hey says"
# print(say)
# multiline="Life is too short\nYou need python"
# print(multiline)
# head = "Python"
# tail = " is fun!"
# print(head + tail)
# a="python"
# print(a*2)
# print("="*50)
# print("My Program")
# print("="*50)
# a="Life is too short, You need python"
# print(len(a))
# a="Life is too short, You need python"
# print(a[3])
# a="Life is too short, You need python"
# print(a[0])
# print(a[12])
# print(a[-1])
# a="Life is too short, you need Python"
# b= a[0] + a[1] + a[2] + a[3]
# print(b)
# print(a[0:4])
# print(a[0:3])
# print(a[0:5])
# print(a[0:2])
# print(a[5:7])
# print(a[12:17])
# print(a[19:])
# print(a[:17])
# print(a[:])
# print(a[19:-7])
# a="20230331Rainy"
# date=a[:8]
# weather=a[8:]
# print(date)
# print(weather)
# year = a[:4]
# day = a[4:8]
# weather = a[8:]
# print(year)
# print(day)
# print(weather)
# a="Pithon"
# print(a[:1])
# print(a[2:])
# print(a[:1] + 'y' + a[2:])
# print("I eat %d apples." % 3)
# print("I eat %s apples." % "five")
# number = 3
# print("I eat %d apples." % number)
# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days" % (number, day))
# print("I have %s apples" % 3)
# print("rate is %s " % 3.234)
# print("%10s" % "hi")
# print("%-10sjane" % 'hi')
# print("%0.4f" % 3.42134234)
# print("%10.4f" % 3.42134234)
# print("I eat {0} apples".format(3))
# print("I eat {0} apples".format("five"))
# number = 3
# print("I eat {0} apples".format(number))
# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days".format(number, day))
# print("I ate {number} apples, so I was sick for {day} days.".format(number=10, day=3))
# print("{0:<10}" .format("hi"))
# print("{0:>10}" .format("hi"))
# print("{0:^10}" .format("hi"))
# print("{0:=^10}" .format("hi"))
# print("{0:!<10}" .format("hi"))
# y=3.42134234
# print("{0:0.4f}" .format(y))
# print("{0:10.4f}" .format(y))
# print("{{ and }}" .format(y))
# name = "홍길동"
# age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# age=30
# print(f'나는 내년이면 {age+1}살이다.')
# d={'name':'홍길동', 'age':30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
# print(f'{"hi":<10}')
# print(f'{"hi":>10}')
# print(f'{"hi":^10}')
# print(f'{"hi":=^10}')
# print(f'{"hi":!<10}')
# y=3.42134234
# print(f'{y:0.4f}')
# print(f'{y:10.4f}')
# print(f'{{ and }}')
# print(f'{"python":!^12}')
# a="hobby"
# print(a.count('b'))
# a="Python is the best choice"
# print(a.find('b'))
# print(a.find('k'))
# a="Life is too short"
# print(a.index('t'))
# # print(a.index('k'))
# print(",".join('abcd'))
# print(",".join(['a','b','c','d']))
# a="hi"
# print(a.upper())
# a="HI"
# print(a.lower())
# a=" hi "
# print(a.lstrip())
# a=" hi "
# print(a.rstrip())
# print(a.strip())
# a="Life is too short"
# print(a.replace("Life", "Your leg"))
# a="Life is too short"
# print(a.split())
# b="a:b:c:d"
# print(b.split(':'))

# ### 2-3. 리스트 자료형
# odd=[1,3,5,7,9]
# a=[]
# b=[1,2,3]
# c=['Life', 'is', 'too', 'short']
# d=[1,2,'Life', 'is']
# e=[1,2,['Life', 'is']]
# a=[1,2,3]
# print(a)
# print(a[0])
# print(a[0] + a[2])
# print(a[-1])
# a=[1,2,3,['a','b','c']]
# print(a[0])
# print(a[-1])
# print(a[3])
# print(a[-1][0])
# print(a[-1][1])
# print(a[-1][2])
# a=[1,2,['a','b',['Life', 'is']]]
# print(a[2][2][0])
# a=[1,2,3,4,5]
# print(a[0:2])
# a="12345"
# print(a[0:2])
# a=[1,2,3,4,5]
# b=a[:2]
# c=a[2:]
# print(b)
# print(c)
# print(a[1:3])
# a=[1,2,3,['a','b','c'],4,5]
# print(a[2:5])
# print(a[3][:2])
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
# a=[1,2,3]
# print(a*3)
# a=[1,2,3]
# print(len(a))
# a=[1,2,3]
# print(str(a[2])+"hi")
# a=[1,2,3]
# a[2]=4
# print(a)
# a=[1,2,3]
# del a[1]
# print(a)
# a=[1,2,3,4,5]
# del a[2:]
# print(a)
# a=[1,2,3]
# a.append(4)
# print(a)
# a.append([5,6])
# print(a)
# a=[1,4,3,2]
# a.sort()
# print(a)
# a=['a','c','b']
# a.sort()
# print(a)
# a=['a','c','b']
# a.reverse()
# print(a)
# a=[1,2,3]
# print(a.index(3))
# print(a.index(1))
# # print(a.index(0))
# a=[1,2,3]
# a.insert(0,4)
# print(a)
# a.insert(3,5)
# print(a)
# a=[1,2,3,1,2,3]
# a.remove(3)
# print(a)
# a.remove(3)
# print(a)
# a=[1,2,3]
# print(a.pop())
# print(a)
# a=[1,2,3]
# print(a.pop(1))
# print(a)
# a=[1,2,3,1]
# print(a.count(1))
# a=[1,2,3]
# a.extend([4,5])
# print(a)
# b=[6,7]
# a.extend(b)
# print(a)

# ### 2-4. 튜플 자료형
# t1=()
# t2=(1,)
# t3=(1,2,3)
# t4=1,2,3
# t5=('a','b',('ab','cd'))
# t1=(1,2,'a','b')
# # del t1[0])
# # print(t1)
# # t1=(1,2,'a','b')
# # t1[0]='c'
# # print(t1)
# t1=(1,2,'a','b')
# print(t1[0])
# print(t1[3])
# t1=(1,2,'a','b')
# print(t1[1:])
# t1=(1,2,'a','b')
# t2=(3,4)
# t3=t1+t2
# print(t3)
# t2=(3,4)
# t3=t2*3
# print(t3)
# t1=(1,2,'a','b')
# print(len(t1))

### 2-5. 딕셔너리 자료형
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
# a={1:'hi'}
# a={'a':[1,2,3]}
# a={1:'a'}
# a[2]='b'
# print(a)
# a['name']='pey'
# print(a)
# a[3]=[1,2,3]
# print(a)
# del a[1]
# print(a)
# grade={'pey':10, 'julliet':99}
# print(grade['pey'])
# print(grade['julliet'])
# a={1:'a', 2:'b'}
# print(a[1])
# print(a[2])
# a={'a':1, 'b':2}
# print(a['a'])
# print(a['b'])
# dic={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
# print(dic['name'])
# print(dic['phone'])
# print(dic['birth'])
# a={1:'a', 1:'b'}
# print(a)
# # a={[1,2]:'hi'}
# # print(a)
# a={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
# print(a.keys())
# for k in a.keys():
#     print(k)
# print(list(a.keys()))
# print(a.values())
# print(a.items())
# a.clear()
# print(a)
# a={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
# print(a.get('name'))
# print(a.get('phone'))
# print(a.get('birth'))
# print(a.get('nokey'))
# # print(a['nokey'])
# print(a.get('nokey', 'foo'))
# a={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
# print('name' in a)
# print('email' in a)
# dic={'name':'pey', 'phone': '010-9999-1234', 'birth':'1118'}

### 2-6. 집합 자료형
# s1=set([1,2,3])
# print(s1)
# s2=set("Hello")
# print(s2)
# s1=set([1,2,3])
# l1=list(s1)
# print(l1)
# print(l1[0])
# t1=tuple(s1)
# print(t1)
# print(t1[0])
# s1=set([1,2,3,4,5,6])
# s2=set([4,5,6,7,8,9])
# print(s1&s2)
# print(s1.intersection(s2))
# print(s1|s2)
# print(s1.union(s2))
# print(s1-s2)
# print(s2-s1)
# print(s1.difference(s2))
# print(s2.difference(s1))
# # s1=set([1,2,3])
# # s1.add(4)
# # print(s1)
# # s1=set([1,2,3])
# # s1.update([4,5,6])
# # print(s1)
# # s1=set([1,2,3])
# # s1.remove(2)
# # print(s1)

# ### 2-7. 불 자료형
# # a=True
# # b=False
# # print(type(a))
# # print(type(b))
# # print(1==1)
# # print(2>1)
# # print(2<1)
# # print(2<1)
# # a=[1,2,3,4]
# # while a:
# #     print(a.pop())
# # if []:
# #     print("참")
# # else:
# #     print("거짓")
# # if [1,2,3]:
# #     print("참")
# # else:
# #     print("거짓")
# # print(bool('python'))
# # print(bool(''))
# # print(bool([1,2,3]))
# # print(bool([]))
# # print(bool(0))
# # print(bool(3))

# ### 2-8. 자료형의 값을 저장하는 공간, 변수
# a=1
# b="python"
# c=[1,2,3]
# a=[1,2,3]
# print(id(a))
# a=[1,2,3]
# b=a
# print(id(a))
# print(id(b))
# print(a is b)
# a[1]=4
# print(a)
# print(b)
# a=[1,2,3]
# b=a[:]
# a[1]=4
# print(a)
# print(b)
# from copy import copy
# a=[1,2,3]
# b=copy(a)
# print(b is a)

# a,b=('python', 'life')
# (a,b)='python', 'Life'
# [a,b]='python', 'Life'
# a=b='python'
# a=3
# b=5
# a,b=b,a
# print(a)
# print(b)


# ### 3-1. If문
# money = True
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
# # money=True
# # if money:
# #     print("택시를 타고 가라")
# # print("타고")
# #     print("가라")
# # money=True
# # if money:
# #     print("택시를")
# #     print("타고")
# #        print("가라")
    
# # money=True
# # if money:

# x=3
# y=2
# print(x>y)
# print(x<y)
# print(x==y)
# print(x!=y)
# money=2000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
# money=2000
# card=True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
# print(1 in [1,2,3])
# print(1 not in [1,2,3])
# print('a' in ('a','b','c'))
# print('j' not in 'python')
# pocket=['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# pocket=['paper', 'cellphone', 'money']
# if 'card' not in pocket:
#     print("걸어가라")
# else:
#     print("버스를 타고 가라")

# pocket=['paper', 'money', 'cellphone']
# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")
# print("앙기모찌")
# pocket = ['paper', 'handphone']
# card = True
# if 'money' in pocket:
#     print("택시를 타고 가라")
# else:
#     if card:
#         print("택시를 타고 가라")
#     else:
#         print("걸어가라")
# pocket=['paper', 'cellphone']
# card=True
# if 'money' in pocket:
#     print("택시를 타고 가라")
# elif card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")
# pocket=['paper', 'money', 'cellphone']
# if 'money' in pocket: pass
# else: print("카드를 꺼내라")

# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
# message = "success" if score >= 60 else "failure"

# ### 3-2 while 문
# treeHit=0
# while treeHit <10:
#     treeHit=treeHit+1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit==10:
#         print("나무 넘어갑니다.")

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number: """
# number=0
# while number != 4:
#     print(prompt)
#     number=int(input())

# coffee = 10
# money=300
# while money:
#     print("돈을 받았으니 커피를 줍니다")
#     coffee=coffee-1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee==0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break
# coffee=10
# while True:
#     money=int(input("돈을 넣어주세요: "))
#     if money==300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money>300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee==0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# a=0
# while a<10:
#     a=a+1
#     if a%2==0: continue
#     print(a)

# a=0
# while a<10:
#     a=a+1
#     if a%3==0: continue
#     print(a)

# a=0
# while a<10:
#     a=a+1
#     if a%3|0: continue
#     print(a)

# ### 3-3 for 문

# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# a=[(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first+last)

# marks = [90, 25, 67, 45, 80]
# number=0
# for mark in marks:
#     number=number+1
#     if mark>=60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# marks=[90, 25, 67, 45, 80]
# number=0
# for mark in marks:
#     number=number+1
#     if mark<60: continue
#     print("%d번 학생 축하합니다. 합격입니다." % number)

# a=range(10)
# print(a)

# a=range(1,11)
# print(a)

# add=0
# for i in range(1,11):
#     add=add+i
# print(add)

# marks=[90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number]<60: continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# add=0
# for i in range(1,101):
#     add=add+i
# print(add)

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end=" ")
#     print('')

# a=[1, 2, 3, 4]
# result=[]
# for num in a:
#     result.append(num*3)
# print(result)

# a=[1, 2, 3, 4]
# result=[num*3 for num in a]
# print(result)

# a=[1, 2, 3, 4]
# result=[num*3 for num in a if num%2==0]
# print(result)

# result=[x*y for x in range(2,10)
#             for y in range(1,10)]
# print(result)

# result=0
# i=1
# while i <=1000:
#     if i%3==0:
#         result += i
#     i += 1
# print(result)

# i=0
# while True:
#     i += 1
#     if i>5: break
#     print('*'*i)

# for i in range(1, 101):
#     print(i)

# A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total=0
# for score in A:
#     total += score
# # average = total/len(A)
# # print(average)

# numbers=[1,2,3,4,5]
# result=[num*2 for num in numbers if num%2==1]
# print(result)

# ### 4-1. 함수

# def 함수_이름(매개변수):
#     수행할_문장1
#     수행할_문장2

# def add(a, b):
#     return a+b
# a=3
# b=4
# c=add(a,b)
# print(c)

# def add(a, b):
#     result=a+b
#     return result
# a=add(3, 4,)
# print(a)

# def say():
#     return 'Hi'
# a=say()
# print(a)

# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
# # print(add(3, 4))

# def say():
#     print('Hi')
# print(say())

# def sub(a, b):
#     return a-b
# result=sub(a=7, b=3)
# print(result)

# result=sub(b=5, a=3)
# print(result)

# def add_many(*args):
#     result=0
#     for i in args:
#         result=result+i
#     return result

# result=add_many(1,2,3)
# print(result)
# result=add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)


# def add_mul(choice, *args):
#     if choice=="add":
#         result=0
#         for i in args:
#             result=result+i
#     elif choice=="mul":
#         result=1
#         for i in args:
#             result=result*i
#     return result

# result=add_mul('add', 1,2,3,4,5)
# print(result)

# result=add_mul('mul', 1,2,3,4,5)
# print(result)

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1)
# print_kwargs(name='foo', age=3)

# def add_and_mul(a, b):
#     return a+b, a*b
# result=add_and_mul(3, 4)
# print(result)

# result1, result2 = add_and_mul(3, 4)

# def add_and_mul(a, b):
#     return a+b
#     return a*b

# result=add_and_mul(2, 3)
# print(result)

# def add_and_mul(a, b):
#     return a+b

# def say_myself(name, age, man=True):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d살입니다." % age)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# print(say_myself("박응용", 27))
# print(say_myself("박응용", 27, True))
# print(say_myself("박응선", 27, False))

# def say_myself(name, man=True, age):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d입니다." % age)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# print(say_myself("박응용", 27))

# a=1
# def vartest(a):
#     a=a+1
# # vartest(a)
# # print(a)

# def vartest(hello):
#     hello = hello + 1

# a=1
# def vartest(a):
#     a=a+1
#     return a
# a= vartest(a)
# print(a)

# a=1
# def vartest():
#     global a
#     a=a+1
# # vartest()
# # print(a)

# add= lambda a, b: a+b
# result=add(3, 4)
# print(result)

# def add(a, b):
#     return a+b
# result=add(3, 4)
# print(result)

# ### 4-2 사용자 입출력

# a= input()
# Life is too short, you need Python
# print(a)

# ### 4-3 파일 읽고 쓰기

# f=open("새파일.txt", "w")
# f.close()

# f=open("/Users/jonghyunlee/Documents/python-study/새파일.txt", 'w')
# f=close()

# f=open("/Users/jonghyunlee/Documents/python-study/새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()




#Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
#Type "help", "copyright", "credits" or "license()" for more information.
#==================================================
#>>> print("My Program")
#My Program
#>>> print("="*50)
#==================================================
