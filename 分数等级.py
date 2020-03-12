# 分数等级.py

score = eval(input("请输入分数："))
if (100 >= score >= 90 ):
    grade = "A"
elif (score >= 80):
    grade = "B"
elif (score >= 70):
    grade = "C"
elif (score >= 60):
    grade = "D"
elif (60> score >= 0):
    grade = "E"

print ("输入的成绩级别为:{}".format(grade))
