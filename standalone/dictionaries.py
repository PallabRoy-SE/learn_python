dic = {"name": "Pallab Roy", "age": 25}

print(dic)

print(dic["name"])
dic["address"] = "Kolkata"
print(dic)
dic.pop("age")
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

dic2 = {i: i**2 for i in range(1, 11)}
print(dic2)
