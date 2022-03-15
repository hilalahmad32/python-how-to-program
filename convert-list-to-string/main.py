
# define a function with argument
from turtle import st


def convertToString(list1):
    str = ""
    for i in list1:
        str += i

    return str


list1 = ["hello ", "myName ", "is ", "hilal ahmad"]
print(type(list1))
string = convertToString(list1)
print(string)
print(type(string))
