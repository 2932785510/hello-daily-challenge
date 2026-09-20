try:
    number = int(input("请输入一个数字: "))
    print(f"你输入的是{number}")
except ValueError:
    print("这不是数字，请重新运行并输入")
try:
    a=int(input("被除数: "))
    b=int(input("除数: "))
    result=a/b
    print(f"结果是{result}")
except ValueError:
    print("请输入数字！")
except ZeroDivisionError:
    print("除数不能为零，请重新运行并输入")
def safe_int(s):
    try:
        return int (s)
    except ValueError:
        return None
num=safe_int(input("输入一个数字: "))
if num==None:
    print("Homura")
else:
    print(f"你输入的是{num}")