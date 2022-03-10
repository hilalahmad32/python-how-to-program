print("Reverse String")

def reverse_string(str):
    str1=""
    for i in str:
        str1=i+str1

    return str1

str="Project World"
print(str)
print(reverse_string(str))