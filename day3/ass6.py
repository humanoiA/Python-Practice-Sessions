str=input("Enter String: ")
if len(str)>=3:
    if str[len(str)-1]=="g" and str[len(str)-2]=="n" and str[len(str)-3]=="i":
        print(str[:len(str)-3]+"ly")
    else:
        print(str+"ing")
else:
    print(str)        

        