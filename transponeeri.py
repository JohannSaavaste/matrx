def transponeeri(maatriks):
    trans=[]
    for x in range(len(maatriks)):
        rida=[]
        for y in maatriks:
            rida.append(y[x])
        trans.append(rida)
    return trans
