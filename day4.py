fruits=["apple","banana"]
print(fruits)
fruits.append("orange")
fruits.append("grape")
fruits.remove("banana")
print(fruits)
for f in fruits:
    print(f"我喜欢吃{f}")
print(f"一共{len(fruits)}种水果")
print(f"第一个：{fruits[0]}")
print(f"最后一个：{fruits[-1]}")
nums=[3,1,4,1,5]
nums.sort()
print(nums)
nums.reverse()
print(nums)