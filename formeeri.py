def formeeri(maatriks):
    suurim=[]
    for x in range(len(maatriks[0])):
        suurim.append(0)
    for x in maatriks:
        indeks=0
        for y in x:
            if suurim[indeks]<len(y):
                suurim[indeks]=len(y)
            indeks+=1

    for x in maatriks:
        valjund=""
        indeks=0
        for y in x:
            valjund+=(suurim[indeks]-len(y))*" "+y+" "
            indeks+=1
        print(valjund)