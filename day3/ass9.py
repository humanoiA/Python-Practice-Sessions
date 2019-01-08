str1= input("Enter String1: ")
str2 = input("Enter String2: ")
count=0
count2=0
if len(str1)==len(str2):
    for i in range(len(str1)):
        if str1[i] in str2:
            count+=1
        else:
            break
    if count==len(str1):
        for i in range(len(str1)):
            if str2[i] in str1:
                count2+=1
            else:
                break
    if count2==len(str1):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")