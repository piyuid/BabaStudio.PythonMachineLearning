#Name : Leo Puji Christyanto
#email : leopuji17@gmail.com

#Latihan 4 [Python - Machine Learning - Babastudio]
#Class function

# class MyClass:
#     nama = "Leo"

# name = MyClass()
# print(name.nama)

class person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age
    
    def myFunc(abc):
        print("Hello Nama Saya adalah " + abc.name)
        print("Umur Saya adalah " + str(abc.age))

run = person("Leo", 30)
run.myFunc()

# print(run.name)
# print(run.age)
