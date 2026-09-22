text=input("请输入一段文字：")
with open("note.txt","w",encoding="utf-8") as f:
    f.write(text)
with open("note.txt","r",encoding="utf-8") as f:
    content=f.read()
print("读回来是：",content)
import json
user={"name":"Homura","age":16,"city":"见陇原"}
with open("user.json","w",encoding="utf-8") as f:
    json.dump(user,f,ensure_ascii=0)
with open("user.json","r",encoding="utf-8") as f:
    loaded=json.load(f)
print(loaded["name"],loaded["age"])
users=[
    {"name":"Homura","age":16},
    {"name":"Madoka","age":15},
    {"name":"Sayaka","age":16}
]
with open("users.json","w",encoding="utf-8") as f:
    json.dump(users,f,ensure_ascii=0)
with open("users.json","r",encoding="utf-8") as f:
    loaded2=json.load(f)
for i in loaded2:
    print(f"用户名为：{i["name"]}")