def determinant(maatriks):
    jar=[]
    f=open(maatriks, "r")
    for x in f:
        x=x.strip().split(" ")
        yl=[]
        for y in x:
            y= float(y)
            yl.append(y)
        jar.append(yl)
    if len(yl)!=len(jar):
        return "Maatriksist determinanti ei saa võtta"
    print(jar)
    f.close()
    for x in range(len(jar)):
        diagonaal=0
        #for y in range(len(x)):
         #   if 