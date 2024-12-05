student_infor = {
    "name": "Devi",
    # "age": 65,
    "age": 67,
    "address": "KA"
}

print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])
student_infor["age"] = 100
print(student_infor)

student_infor2 = dict(name="Devi", age=67, address="KA")


student_infor1 = {
    "name": "Devi",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Praveen",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}