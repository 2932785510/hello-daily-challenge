class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name}：汪！")
    def intro(self):
        print(f"我是{self.breed}，叫{self.name}。")
d1=Dog("旺财","金毛")
d2=Dog("小黑","柯基")
d1.bark()
d2.bark()
d1.intro()
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greed(self):
        print(f"我叫{self.name},今年{self.age}岁")
user1=user("Homura",16)
user2=user("Madoka",15)
user1.greed()
user2.greed()