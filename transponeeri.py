def transponeeri(maatriks):
    f=open(maatriks, "r")
    jar=[]
    for x in f:
        x=x.strip().split(" ")
        jar.append(x)

    trans=[]
    for x in range(len(jar)):
        rida=[]
        for y in jar:
            rida.append(y[x])
        trans.append(rida)

    for x in trans:
        valjund=""
        for y in x:
            valjund+=y
        valjund+="\n"
        print(valjund)