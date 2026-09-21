class Animals:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("...")
    def __str__(self):
        return self.name
    def info(self):
        print("我是动物")
class Dog(Animals):
    def speak(self):
        print(f"{self.name}：汪汪！")
    def info(self):
        print("我是狗")
        super().info()
class Cat(Animals):
    def speak(self):
        print(f"{self.name}：喵喵！")
d=Dog("旺财")
c=Cat("咪咪")
d.speak()
c.speak()
print(d)
d.info()