a = int(input())
b = int(input())
c = int(input())

score = int(a+b+c)

if (score>=80) and (score<=100):
    print("A")
elif (score>=75) and (score<=79):
    print("B+")
elif (score>=70) and (score<=74):
    print("B")
elif (score>=65) and (score<=69):
    print("C+")
elif (score>=60) and (score<=64):
    print("C")
elif (score>=55) and (score<=59):
    print("D+")
elif (score>=50) and (score<=54):
    print("D")
else:
    print("F")