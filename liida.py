def liida(m1, m2):
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        return "Maatrikseid ei saa liita"
    else:
        summa=[]
        for x in range(len(m1)):
            rida=[]
            for y in range(len(m1[0])):
                arv=float(m1[x][y])+float(m2[x][y])
                if arv%1==0:
                    arv=int(arv)
                rida.append(str(arv))
            summa.append(rida)
    return summa