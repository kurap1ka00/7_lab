def find_mm(str):
    bfint=0
    bfstr=''
    for i in range(1, int(len(str)/2)-1):
        for j in range(0,i):
            if(str.count(str[j:i])>=bfint):
                bfint=str.count(str[j:i])
                bfstr=str[j:i]
    return bfint, bfstr        
    

st = input()
print(find_mm(st))
