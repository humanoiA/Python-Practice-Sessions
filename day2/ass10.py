c=input("Enter Character: ")
if ord(c)>=97 and ord(c)<=122:
    print("Lower Case Letter")
elif ord(c)>=65 and ord(c)<=90:
    print("Upper Case Letter")
elif ord(c)>=48 and ord(c)<=57:
    print("Digit")
else:
    print("Special Symbol")
    