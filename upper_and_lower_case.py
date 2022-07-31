from ctypes.wintypes import WORD


def string_test(str1):
    sub={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in str1:
        if c.isupper():
           sub["UPPER_CASE"]+=1
        elif c.islower():
           sub["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", str1)
    print ("No. of Upper case characters : ", sub["UPPER_CASE"])
    print ("No. of Lower case Characters : ", sub["LOWER_CASE"])
string_test('The quick Brown Fox')