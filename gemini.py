import re
s = '-1@10@-1#10@2@10#-1@10@-1'
l=s.split('#')
result=list()
for i in l:
    k = [int(d) for d in re.findall(r'-?\d+', i)]
    result.append(k)
exp=result
for i in range(len(exp)):
    for j in range(len(i)):
        if exp[i][j]==-1:
            if exp[i+1][j]==-1 or exp[i][j+1]==-1 or exp[i+1][j+1]==-1 or exp[i-1][j]==-1 or exp[i][j-1]==-1 or exp[i-1][j-1]==-1:
                

