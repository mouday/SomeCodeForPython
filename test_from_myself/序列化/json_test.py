
import json

dct = {
    "std1": {"name":"Tom", "age": 23, "city": "beijing"},
    "std2": {"name":"Jack", "age": 24, "city": "hunan"},
    "std3": {"name":"Jimi", "age": 25, "city": "wuhang"}
}

with open("students.json", "w") as f:
    json.dump(dct, f, indent="\t")  # 增加缩进

print("ok")
