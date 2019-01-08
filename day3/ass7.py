str=input("Enter String: ")
if len(str)%4==0:
    print(str[-1:-len(str)-1:-1])
else:
    print("Length issue")