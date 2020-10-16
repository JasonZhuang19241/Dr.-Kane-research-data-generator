import math
import sys
a=input("sure to continue? ")
lists=[(1,1,1,1),(1,1,1,2),(1,1,1,3),(1,1,1,4),(1,1,1,5),(1,1,2,2),(1,1,2,3),(1,1,2,4),(1,1,2,6),(1,1,3,3),(1,2,2,2),(1,2,2,3),(1,2,2,4),(1,2,2,6),(1,2,4,4),(1,2,4,6)]
length=len(lists)
for i in range(length):
    a=i+1
    write="["+"="*a+">"+" "*(length-a)+"] "+str(a)+"/"+str(length)
    sys.stdout.write("\r" + write)
    sys.stdout.flush()
    f = open(str(lists[i])+'.txt','w')
    s = [] # s[i] represents the number of solutions for n = i
    a = lists[i]
    f.write(str(a))
    f.write("\r")
    def value(x1,x2,x3,x4):
        return a[0]*(x1**2)+a[1]*(x2**2)+a[2]*(x3**2)+a[3]*(x4**2)
    def weight(x1,x2,x3,x4):
        time = 1
        if x1 != 0:
            time = time * 2
        if x2 != 0:
            time = time * 2
        if x3 != 0:
            time = time * 2
        if x4 != 0:
            time = time * 2
        return time

    for n in range(0,1001): # take range of n as 0-1000
        result = 0
        for x1 in range(0,int(math.sqrt(n))+1):
            if value(x1,0,0,0) > n:
                break
            for x2 in range(0,int(math.sqrt(n))+1):
                if value(x1,x2,0,0) > n:
                    break
                for x3 in range(0,int(math.sqrt(n))+1):
                    if value(x1,x2,x3,0) > n:
                        break
                    for x4 in range(0,int(math.sqrt(n))+1):
                        if value(x1,x2,x3,x4) == n:
                            result = result + 1*weight(x1,x2,x3,x4)
        s.append(result)
        f.writelines(str(result))
        f.write('\n')


        
    f.close()
