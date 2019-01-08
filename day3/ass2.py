str= input("Enter String : ")
for i in range(len(str)):
    if str[i] not in str[:i]:
        print(str[i]+' occurs ')
        print(str.count(str[i]))