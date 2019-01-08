str= input("Enter String : ")
ch= input("Enter Char: ")
s1=str[:str.index(ch)+1]
s2=str[str.index(ch)+1:].replace(ch,"$")
str=s1+s2
print(str)