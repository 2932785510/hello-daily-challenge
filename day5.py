user={"name": "Homura", "age": 16, "city": "见陇原"}
print(user["name"])
print(user["age"])
user["age"]=17
user["hoppy"]="Madoka"
del user["city"]
print(user)
for k,val in user.items():
    print(f"key={k},value={val}")
print(user.get("city"))
print(user.get("city","未知"))
user2=[
    {"name":"Homura","age":16},
    {"name":"Madoka","age":15},
    {"name":"Sayaka","age":16}
]
for u in user2:
    print(f"{u['name']}今年{u['age']}岁")