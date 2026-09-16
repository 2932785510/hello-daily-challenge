age=int(input("请输入你的年龄:"))
if age<=0:
    print("别开玩笑了！")
elif age<=18:
    print("未成年")
elif age<=60:
    print("成年")
else:
    print("老年")
score=int(input("请输入你的分数:"))
if score>=90:
    print("优秀")
elif score>=60:
    print("及格")
else:
    print("不及格")