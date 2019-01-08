str1= input("Enter String1: ")
str2 = input("Enter String2: ")
sum1=0
sum2=0
if len(str1)>len(str2):
    print(str1)
elif len(str1)==len(str2):
    for i in range(len(str1)):
        sum1+=ord(str1[i])
        sum2+=ord(str2[i])
    if sum1>sum2:
        print(str1)
    else:
        print(str2)
else:
    print(str2)