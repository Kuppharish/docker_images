import numpy as np
ply_path = "model.ply"
test_ply = "test.ply"
f = open(ply_path, 'r')
f1 = open(test_ply,'w')
while True:
    elems = f.readline().rstrip('\n').rstrip('\r').split()
    if(len(elems)!=10):
        f1.write(f.readline())
    else:
        stri = ""
        for i in range(len(elems)-1):
            stri+=str(elems[i])
            stri+=" "
        stri+="\n"
        f1.write(stri)