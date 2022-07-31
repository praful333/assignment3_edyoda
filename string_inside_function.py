def StrInverse(str1):
    str2 = str1[::-1]
    return str2

a = input("Please enter word : ")

b = StrInverse(a)
print("Original = ", a)
print("After = ", b)