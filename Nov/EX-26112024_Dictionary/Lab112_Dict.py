dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)

# Sort a dictionary by its values in descending order
my_dict = {"a": 3, "b": 1, "c": 2}

# {b: 1 , c: 2 , a :3}

myDict={"a":10,"b":20,"c":30}
myKeys=myDict.values()
print(sorted(myKeys))  # sorts in ascending order
print(sorted(myKeys,reverse=True)) # sorts in  desending order