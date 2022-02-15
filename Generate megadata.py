import os
import time
import math,sys
import shutil
lists=[(1,1,1,1),(1,1,1,2),(1,1,1,3),(1,1,1,4),(1,1,1,5),(1,1,2,2),(1,1,2,3),(1,1,2,4),(1,1,2,6),(1,1,3,3),(1,2,2,2),(1,2,2,3),(1,2,2,4),(1,2,2,6),(1,2,4,4),(1,2,4,6)]
def value(x1, x2, x3, x4):
    global a
    return a[0] * (x1 ** 2) + a[1] * (x2 ** 2) + a[2] * (x3 ** 2) + a[3] * (x4 ** 2)

for i in range(len(lists)):
    a=lists[i]
    file_name="meta"+str(a)+".txt";print(file_name)
    txt_file = open(file_name, "w+")
    txt_file.close()
    txt_file=open(file_name,"w+")
    for n in range(0, 101):  # take range of n as 0-1000
        txt_file.write("*\n")
        write = "[" + "=" * int(n/10) + ">" + " " * int((100 - n)/10) + "] " + str(i+1) + "/" + str(16)
        sys.stdout.write("\r" + write)
        sys.stdout.flush()
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
    shutil.move(file_name,"metadata/"+file_name)

