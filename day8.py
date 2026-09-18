def add(a,b):
    return a + b
print(add(3,5))
print(add(10,20))
def greet(name):
    return(f"你好，{name}!")
print(greet("Homura"))
def greet2(name="朋友"):
    return(f"你好，{name}!")
print(greet2())
print(greet2("Madoka"))
def is_adult(age):
    return age >=18
for i in (15,20,25):
    print(f"{i}岁"+("成年"if is_adult(i) else "未成年"))