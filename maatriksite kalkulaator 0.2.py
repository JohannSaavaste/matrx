def tagasta_maatriks(fail):  #Loeb tekstifailist maatriksi read
    f=open(fail, "r")
    jar=[]
    for x in f:
        y=x.strip().split(" ")
        jar.append(y)
    return jar

def sisesta_maatriks():  #Laseb kasutajal käsitsi sisestada maatriksi elemendid
    rida=int(input('Sisesta ridade arv: '))
    veerg=int(input('Sisesta veergude arv: '))
    maatriks=[]
    for i in range(rida):
        rida=[]
        for j in range(veerg):
            liige=int(input('Sisesta liige: '))
            rida.append(liige)
        maatriks.append(rida)
    return maatriks

def transponeeri(maatriks):
    trans=[]
    for z in maatriks:    
        for x in range(len(z)):
            rida=[]
            for y in maatriks:
                rida.append(y[x])
            trans.append(rida)
        return trans
    
def liida(m1, m2):  #Liidab maatriksid omavahel
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

def lahuta(m1, m2): #Lahutab maatriksid omavahel
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        return "Maatrikseid ei saa liita"
    else:
        vahe=[]
        for x in range(len(m1)):
            rida=[]
            for y in range(len(m1[0])):
                arv=float(m1[x][y])-float(m2[x][y])
                if arv%1==0:
                    arv=int(arv)
                rida.append(str(arv))
            vahe.append(rida)
    return vahe

def korruta(m1,m2): #Korrutab maatriksid
    if len(m2)!=len(m1[0]):
        return "Maatrikseid ei ole võimalik korrutada"
    else:
        korrutis=[]
        for x in range(len(m1)):
            rida=[]
            for y in range(len(m2[0])):
                element=0
                for z in range(len(m1[0])):
                    element+=float(m1[x][z])*float(m2[z][y])
                rida.append(element)
            korrutis.append(rida)
        return korrutis
    
def leia_det(m, n): #Leiab determinandi
    if n==2:
        sarrus=float(m[0][0])*float(m[1][1])-float(m[0][1])*float(m[1][0])
        return sarrus
    else:
        det=0
        for x in range(len(m[0])):
            alammaatriks=[]
            for y in range(1,len(m)):
                lisatav=[]
                for z in range(len(m)):
                    if z!=x:
                        lisatav.append(m[y][z])
                alammaatriks.append(lisatav)
            det+= float(m[0][x])*(-1)**x*leia_det(alammaatriks, n-1)
        return det
def determinant(maatriks): #Määrab, kas determinant leidub
    if len(maatriks)==len(maatriks[0]):
        return leia_det(maatriks, len(maatriks))
    else:
        return "Maatriksist ei saa determinanti leida."

def formeeri(maatriks): #Maatriksi printimine ilusas formaadis
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

kask=input("Programmi käsud: +, -, *, D, T ")
kasud=["+","-","*","D","T"]
while kask in kasud:
    if kask=="+":
        f1=input("Sisesta esimese maatriksi tekstidokumendi nimi: ")
        f2=input("Sisesta teise maatriksi tekstidokumendi nimi: ")
        m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
        uus_maatriks=liida(m1, m2)
        formeeri(uus_maatriks)
    elif kask=="-":
        f1=input("Sisesta esimese maatriksi tekstidokumendi nimi: ")
        f2=input("Sisesta teise maatriksi tekstidokumendi nimi: ")
        m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
        uus_maatriks=lahuta(m1, m2)
        formeeri(uus_maatriks)
    elif kask=="*":
        f1=input("Sisesta esimese maatriksi tekstidokumendi nimi: ")
        f2=input("Sisesta teise maatriksi tekstidokumendi nimi: ")
        m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
        uus_maatriks=korruta(m1, m2)
        formeeri(uus_maatriks)
    elif kask=="D":
        f=input("Sisesta maatriksi tekstidokumendi nimi: ")
        m=tagasta_maatriks(f)
        determinant=determinant(m)
        print(determinant)
    elif kask=="T":
        f=input("Sisesta maatriksi tekstidokumendi nimi: ")
        m=tagasta_maatriks(f)
        uus_maatriks=transponeeri(m)
        formeeri(uus_maatriks)
    kask=input("Programmi käsud: +, -, *, D, T või muu sümbol lõpetamiseks ")
    