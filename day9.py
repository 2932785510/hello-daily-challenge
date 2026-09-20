import random
import time
target=random.randint(1,10)
print("我想到了一个1-10之间的数，你猜猜看！")
startguess=time.time()
for i in range(5):
    guess=int(input("你的猜测是："))
    if guess==target:
        print("猜对了！")
        break
    elif guess<target:
        print("小了，再大点！")
    else:
        print("大了，再小点！")
else:
    print("5次机会已用尽！")
endguess=time.time()
print(f"共用时{endguess-startguess}秒")