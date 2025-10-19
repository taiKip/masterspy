my_dict = {"name": "Alice", "age": 35, "city": "New York", "profession": "Doctor"}

del my_dict["profession"]

print(f"Updated dictionary after removing 'Profession' {my_dict}")
print("Printing all key-value pairs")

for key, value in my_dict.items():
    print(f"{key}:{value}")


def checkForKey(key, dict):
    if key in dict:
        return True
    else:
        return False


print(f"Does 'age' exist? {checkForKey('age',my_dict)}")


keys = ['Ten','Twenty','Thirty']
values = [10,20,30]

res_dic = dict(zip(keys,values))

print(res_dic)