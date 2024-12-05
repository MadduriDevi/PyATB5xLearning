class  person:
    def __init__(self,name):
        self.name =name

    def walk(self):
        return self.name

Devi = person ("Devi")
Praveen = person ("Praveen")

print (Devi.name)
print (Praveen.name)

print("who is walking ",Devi.walk())
print("who is walking ",Praveen .walk())