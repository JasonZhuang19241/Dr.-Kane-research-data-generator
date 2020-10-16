import math
import os, sys
import shutil
divid=int(input("input N wanted: "))
number_array=[]
for n1 in range(0,divid):
    for n2 in range(0,divid):
        for n3 in range(0,divid):
            for n4 in range(0,divid):
                number_array.append([n1,n2,n3,n4])
none_existed=0
try:
    os.mkdir('N='+str(divid))
except:
    none_existed=1
lists=[(1,1,1,1),(1,1,1,2),(1,1,1,3),(1,1,1,4),(1,1,1,5),(1,1,2,2),(1,1,2,3),(1,1,2,4),(1,1,2,6),(1,1,3,3),(1,2,2,2),(1,2,2,3),(1,2,2,4),(1,2,2,6),(1,2,4,4),(1,2,4,6)]
done_number=0
done_names=[]
if none_existed==1:
    for file in os.listdir('N='+str(divid)+'/txt'):
        done_number+=1
        done_names.append(file)
    print("have already finished: "+str(done_names))
    for i in range(done_number-1):
        lists.pop(0)
else:
    print("have no database, creating")
for k in range(len(lists)-1):
    try:
        os.mkdir('N='+str(divid)+"/txt")
    except:
        noti=0
    A='N='+str(divid)+'/txt/'+str(lists[k])+'/'
    try:
        os.mkdir(A)
    except:
        a='skip'
    
    
    for i in range(divid**4):
        display=int((i/(divid**4))*144)
        h=number_array[i]
        write="["+"="*display+">"+" "*(144-display)+"] "+str(k)+"/"+str(16)
        sys.stdout.write("\r" + write)
        sys.stdout.flush()
        hname=os.path.join(A,('h'+'='+str(h))+".txt")
        f = open(hname,'w')
        s = [] # s[i] represents the number of solutions for n = i
        
        a = lists[k]

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
                if x1 % divid != h[0]:
                    continue
                if value(x1,0,0,0) > n:
                    break
                for x2 in range(0,int(math.sqrt(n))+1):
                    if x2 % divid != h[1]:
                        continue
                    if value(x1,x2,0,0) > n:
                        break
                    for x3 in range(0,int(math.sqrt(n))+1):
                        if x3 % divid != h[2]:
                            continue
                        if value(x1,x2,x3,0) > n:
                            break
                        for x4 in range(0,int(math.sqrt(n))+1):
                            if x4 % divid != h[3]:
                                continue
                            if value(x1,x2,x3,x4) == n:
                                result = result + 1*weight(x1,x2,x3,x4)
            s.append(result)
            f.writelines(str(result))
            f.write("\n")

            
        f.close()
print("==============================================")
print("start excel compiling")
import os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def excel_style(col):
    """ Convert given row and column number to an Excel-style cell name. """
    result = []
    while col:
        col, rem = divmod(col-1, 26)
        result[:0] = LETTERS[rem]
    return ''.join(result)
excel_names=[]
for i in range(2*(divid**4+10)):
    excel_names.append(excel_style(i+1))
listr=[(1,1,1,1),(1,1,1,2),(1,1,1,3),(1,1,1,4),(1,1,1,5),(1,1,2,2),(1,1,2,3),(1,1,2,4),(1,1,2,6),(1,1,3,3),(1,2,2,2),(1,2,2,3),(1,2,2,4),(1,2,2,6),(1,2,4,4),(1,2,4,6)]


from openpyxl import Workbook
import openpyxl
for k in range(16):
    print(listr[k])
    names=[]
    datas=[]
    data=[]
    number=0
    for file in os.listdir('N='+str(divid)+'/txt/'+str(listr[k])):
        number+=1
        names.append(file[:-4])
    print(number)
    try:
        book = openpyxl.load_workbook('N='+str(divid)+'.xlsx')
    except:
        wb = Workbook()
        wb.save('N='+str(divid)+'.xlsx')
        book = openpyxl.load_workbook('N='+str(divid)+'.xlsx')
    sheet = book.create_sheet(str(listr[k]))

    sheet['A1'] = "n"
    for i in range(2,1003):
        write1="A"+str(i)
        sheet[write1]=str(i-1)
    sheet['B1'] = "a="+str(listr[k])
    filename=str(listr[k])+".txt"
    file=open(filename, "r+")
    with open(filename, "r") as fps:
        datas = fps.readlines()
    for i in range(2,1003):
        write6="B"+str(i)
        sheet[write6]=datas[i-1]
    file.close()

    for i in range(divid**4):
        write3=str(excel_names[2*(i+1)])+str(1)
        write4=str(names[i])
        sheet[write3]=write4
        txtname='N='+str(divid)+"/txt/"+str(listr[k])+"/"+str(names[i])+".txt"
        file1 = open(txtname,"r+")
        with open(txtname, "r") as fp:
            data = fp.readlines()
        for j in range(2,1003):
            write2=str(excel_names[2*(i+1)])+str(j)
            sheet[write2]=data[j-2][:-1]
            write7=str(excel_names[2*(i+1)+1])+str(j)
            if int(data[j-2][:-1])!=0:
                sheet[write7]=str(int(datas[j-1])/int(data[j-2][:-1]))
            else:
                sheet[write7]="null"
    book.save('N='+str(divid)+'.xlsx')
    original='N='+str(divid)+'.xlsx'
    target='datastorage_'+original
    shutil.copyfile(original, target)
    file1.close()
shutil.move(('N='+str(divid)+'.xlsx'),('N='+str(divid)))
