def transponeeri(maatriks):
    trans=[]
    for z in maatriks:    
        for x in range(len(z)):
            rida=[]
            for y in maatriks:
                rida.append(y[x])
            trans.append(rida)
        return trans
