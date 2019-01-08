str= input("Enter String : ")
if len(str)<2:
    print(str)
else:
    print(str[0:2]+str[len(str)-2:len(str)])
