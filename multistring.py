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
# s1=set([1,2,3])
# s1.add(4)
# print(s1)
# s1=set([1,2,3])
# s1.update([4,5,6])
# print(s1)
# s1=set([1,2,3])
# s1.remove(2)
# print(s1)

### 2-7. 불 자료형
# a=True
# b=False
# print(type(a))
# print(type(b))
# print(1==1)
# print(2>1)
# print(2<1)
# print(2<1)
# a=[1,2,3,4]
# while a:
#     print(a.pop())
# if []:
#     print("참")
# else:
#     print("거짓")
# if [1,2,3]:
#     print("참")
# else:
#     print("거짓")
# print(bool('python'))
# print(bool(''))
# print(bool([1,2,3]))
# print(bool([]))
# print(bool(0))
# print(bool(3))

### 2-8. 자료형의 값을 저장하는 공간, 변수
a=1
b="python"
c=[1,2,3]
a=[1,2,3]
print(id(a))




#Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
#Type "help", "copyright", "credits" or "license()" for more information.
#==================================================
#>>> print("My Program")
#My Program
#>>> print("="*50)
#==================================================
