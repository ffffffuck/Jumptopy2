a=['이유덕','이재영','권종표','이재영','박민호','강상희','이재영','김지완','최승혁','이성연','박영서','박민호','전경헌','송정환','김재성','이유덕','전경헌']

#1
print("김씨와 이씨는 각각 몇명 인가요?")
n=[ i[0] for i in a ]
print("김씨 : %s명\n이씨 : %s명\n" %(n.count("김"), n.count("이")))
print(n.count("김"))

#2
print()
print("'이재영'이란 이름이 몇번 반복되나요?")
d=a.count('이재영')

print("%s번째 입니다" %d)
#3
print()
print("중복을 제거한 이름을 출력하세요")

b=set(a)

c=list(b)

print(c)
#4
print()
print("중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요")
c.sort()

print(c)

