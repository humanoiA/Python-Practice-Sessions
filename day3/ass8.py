str=input("Enter String: ")
c=input("Enter Char: ")
if c in str[:len(c)+1]:
    print("starts with "+c)
else:
    print("does not starts with "+c)