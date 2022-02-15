N=0
number_array=[]
divid=0
h=0
def makenewdivid(number):
    global N, number_array, divid
    number_array=[]
    divid=N
    for n1 in range(0,divid):
        for n2 in range(0,divid):
            for n3 in range(0,divid):
                for n4 in range(0,divid):
                    number_array.append([n1,n2,n3,n4])
    
import os
import time
a=0
import math,sys
import shutil
lists=[(1,1,1,1),(1,1,1,2),(1,1,1,3),(1,1,1,4),(1,1,1,5),(1,1,2,2),(1,1,2,3),(1,1,2,4),(1,1,2,6),(1,1,3,3),(1,2,2,2),(1,2,2,3),(1,2,2,4),(1,2,2,6),(1,2,4,4),(1,2,4,6)]
def value(x1, x2, x3, x4):
    global a
    return a[0] * (x1 ** 2) + a[1] * (x2 ** 2) + a[2] * (x3 ** 2) + a[3] * (x4 ** 2)

def makemeta(testnumber,stopnumber, tuplelist):
    global a
    a=tuplelist
    file_name="meta"+str(a)+".txt";print(file_name)
    try:
        os.remove(file_name)
    except:
        aas=True
    txt_file=open(file_name,"w+")
    for n in range(testnumber, stopnumber):  # take range of n as 0-1000
        txt_file.write("*\n")
        if n%100==0:
            print(n)
        result = 0
        for x1 in range(0, int(math.sqrt(n)) + 1):
            if value(x1, 0, 0, 0) > n:
                break
            for x2 in range(0, int(math.sqrt(n)) + 1):
                if value(x1, x2, 0, 0) > n:
                    break
                for x3 in range(0, int(math.sqrt(n)) + 1):
                    if value(x1, x2, x3, 0) > n:
                        break
                    for x4 in range(0, int(math.sqrt(n)) + 1):
                        if value(x1, x2, x3, x4) == n:
                            tupled=[x1,x2,x3,x4]
                            txt_file.write(str(tupled)+"\n")
    txt_file.close()
    print("done")


def dirchilt(det,m):
    if det==5:
        if m%det==1 or m%det==4:
            return 1
        elif m%det==0:
            return 0
        else:
            return -1
    elif det==8:
        if m%det==1 or m%det==7:
            return 1
        elif m%det==3 or m%det==5:
            return -1
        else:
            return 0
    elif det==12:
        if m%det==1 or m%det==11:
            return 1
        elif m%det==5 or m%det==7:
            return -1
        else:
            return 0
    elif det==-3:
        if m%int(det)==1:
            return -1
        elif m%int(det)==-1:
            return 1
        else:
            return 0
    elif det==-4:
        if m%int(det)==1:
            return -1
        elif m%int(det)==-1:
            return 1
        else:
            return 0

        
def modufunction(choice,n):
    if choice==1:
        sumofm=0
        for i in range(n+1):
            m=int(i+1)
            if n%m==0 and m%4!=0:
                sumofm+=m
        return sumofm*8
    elif choice==2:
        sumofm=0
        for i in range(n):
            m=int(i+1)
            if n%m==0:
                sumofm+=-2*dirchilt(8,m)*m+8*dirchilt(8,n/m)*m
        return sumofm
    elif choice==3:
        sumofm=0
        for i in range(n):
            m=int(i+1)
            if n%m==0:
                sumofm+=-1*dirchilt(12,m)*m+6*dirchilt(12,n/m)*m+3*dirchilt(-3,n/m)*dirchilt(-4,m)*m-2*dirchilt(-4,n/m)*dirchilt(-3,m)*m
        return sumofm    
    
def judgingwithmodu(k, testnumber, stopmember):
    arraytoreturn=[]
    for i in range(testnumber,stopmember-1):
        returnedvalue=modufunction(k+1,i)
        arraytoreturn.append(returnedvalue)
    return arraytoreturn

def judge(x1,x2,x3,x4):
    global N, h
    if x1 % N == h[0] and x2 % N == h[1] and x3 % N == h[2] and x4 % N == h[3]:
        return True
    else:
        return False
def judgingwhole(k):
    global h, N, number_array,divid
    arrayofdata=[]
    try:
        os.mkdir('N='+str(divid)+"/txt")
    except:
        noti=0
    A='N='+str(divid)+'/txt/'+str(lists[k])+'/'
    try:
        os.mkdir(A)
    except:
        a='skip'
    timeappending=0
    print("checking...")
    for i in range((divid)**4):
        timeappending+=1
        h=number_array[i]

        s = [] # s[i] represents the number of solutions for n = i
        
        a = lists[k]
        from ast import literal_eval
        fin = open('meta'+str(a)+'.txt','r')
        lines = fin.readlines()
        ans = [] # ans[i] represents the number of solutions for n = i

        def judge(x1,x2,x3,x4):
            if x1 % N == h[0] and x2 % N == h[1] and x3 % N == h[2] and x4 % N == h[3]:
                return True
            else:
                return False

        n = 0
        result = 0
        for line in lines:
            if line == '*\n':
                n += 1
                
                if timeappending==1:
                    arrayofdata.append(result)
                else:
                    arrayofdata[n-1]+=result
                result = 0
                continue
            line = literal_eval(line[:-1])
            x1 = int(line[0])
            x2 = int(line[1])
            x3 = int(line[2])
            x4 = int(line[3])
            if x1 == 0:
                if x2 == 0:
                    if x3 == 0:
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                    else:  # x3 != 0
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, -x4):
                                result += 1
                else:  # x2 != 0
                    if x3 == 0:
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, -x4):
                                result += 1
                    else:  # x3 != 0
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, -x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, -x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, -x4):
                                result += 1
                            if judge(x1, -x2, -x3, x4):
                                result += 1
                            if judge(x1, -x2, -x3, -x4):
                                result += 1
            else:  # x1 != 0
                if x2 == 0:
                    if x3 == 0:
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, -x4):
                                result += 1
                    else:  # x3 != 0
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, -x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, -x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, -x4):
                                result += 1
                            if judge(-x1, x2, -x3, x4):
                                result += 1
                            if judge(-x1, x2, -x3, -x4):
                                result += 1
                else:  # x2 != 0
                    if x3 == 0:
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, -x2, x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, -x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, -x4):
                                result += 1
                            if judge(-x1, -x2, x3, x4):
                                result += 1
                            if judge(-x1, -x2, x3, -x4):
                                result += 1
                    else:  # x3 != 0
                        if x4 == 0:
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, -x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, -x3, x4):
                                result += 1
                            if judge(-x1, -x2, x3, x4):
                                result += 1
                            if judge(-x1, -x2, -x3, x4):
                                result += 1
                        else:  # x4 != 0
                            if judge(x1, x2, x3, x4):
                                result += 1
                            if judge(x1, x2, x3, -x4):
                                result += 1
                            if judge(x1, x2, -x3, x4):
                                result += 1
                            if judge(x1, x2, -x3, -x4):
                                result += 1
                            if judge(x1, -x2, x3, x4):
                                result += 1
                            if judge(x1, -x2, x3, -x4):
                                result += 1
                            if judge(x1, -x2, -x3, x4):
                                result += 1
                            if judge(x1, -x2, -x3, -x4):
                                result += 1
                            if judge(-x1, x2, x3, x4):
                                result += 1
                            if judge(-x1, x2, x3, -x4):
                                result += 1
                            if judge(-x1, x2, -x3, x4):
                                result += 1
                            if judge(-x1, x2, -x3, -x4):
                                result += 1
                            if judge(-x1, -x2, x3, x4):
                                result += 1
                            if judge(-x1, -x2, x3, -x4):
                                result += 1
                            if judge(-x1, -x2, -x3, x4):
                                result += 1
                            if judge(-x1, -x2, -x3, -x4):
                                result += 1
            
    os.remove("data.txt")
    datainput = open('data.txt','w+')
    datainput.write(str(arrayofdata))
    datainput.close()
    return arrayofdata


print("started")
startpoint=int(input("number needed to check: "))
judgewhich=int(input("which series to check: "))
middepoint=int(input("Start point"))
N=int(input("The value of N: "))
mid=int(middepoint/100)
totalnumber=int(int(startpoint/100)*100)
makenewdivid(N)
for i in range(mid,int(totalnumber/100)):
    judgenumber=100*(i)
    stopwhich=judgenumber+100
    makemeta(judgenumber,stopwhich, lists[judgewhich])
    arrayofdata=judgingwhole(judgewhich)
    try:
        arrayofdata.remove(0)
    except:
        aasds=9
    modujudge=judgingwithmodu(judgewhich,judgenumber,stopwhich)
    trueorfalse=True
    for i in range(1,len(arrayofdata)-1):
        check=i
        if modujudge[check]!=arrayofdata[check]:
            print("False",check)
            trueorfalse=False
    print(trueorfalse)
print("finished checking---")
print(arrayofdata)
a=input()

