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
            liige=int(input('Sisesta ' +str(i+1)+'. rea '+str(j+1)+'. element: '))
            rida.append(liige)
        maatriks.append(rida)
    return maatriks

def transponeeri(maatriks): #Transponeerib maatriksi
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
        return "Maatrikseid ei saa lahutada"
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
                if element%1==0:
                    element=int(element)
                rida.append(element)
            korrutis.append(rida)
        return korrutis
    
def determinant(maatriks): #Määrab, kas determinant leidub
    if len(maatriks)==len(maatriks[0]):
        return leia_det(maatriks, len(maatriks))
    else:
        return "Maatriksist ei saa determinanti leida."

def leia_det(m, n): #Leiab determinandi
    if n==2:
        sarrus=float(m[0][0])*float(m[1][1])-float(m[0][1])*float(m[1][0])
        if sarrus%1==0:
            det=int(sarrus)
        return det
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
        if det%1==0:
            det=int(det)
        return det

def formeeri(maatriks): #Väljastab maatriksi ekraanile
    if isinstance(maatriks, list):
        suurim=[]
        for x in range(len(maatriks[0])):
            suurim.append(0)
        for x in maatriks:
            indeks=0
            for y in x:
                if suurim[indeks]<len(str(y)):
                    suurim[indeks]=len(str(y))
                indeks+=1

        for x in maatriks:
            valjund=""
            indeks=0
            for y in x:
                valjund+=(suurim[indeks]-len(str(y)))*" "+str(y)+" "
                indeks+=1
            print(valjund)
    else:
        print(maatriks)


print('Saadaval on järgmised tehted:')
print('-liitmine(+)\n-lahutamine(-)\n-korrutamine(*)\n-transponeerimine(T)\n-determinandi leidmine(D)')
käsk=input('Millist tehet soovid sooritada?: ')
käsud=["+","-","*","D","T", 'd', 't', 'liitmine', 'lahutamine', 'korrutamine', 'determinant',
       'determinandi leidmine', 'transponeerimine']

while käsk in käsud:
    sisestamisviis=input('Kas sooviksid maatriksi sisestada failina või käsitsi? (f/k): ')
    if sisestamisviis=='failina' or sisestamisviis=='f':
        if käsk=="+" or käsk.lower()=='liitmine':
            f1=input("Sisesta esimese maatriksi tekstidokumendi nimi:")
            f2=input("Sisesta teise maatriksi tekstidokumendi nimi:")
            m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
            formeeri(m1)
            print('+')
            formeeri(m2)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=liida(m1, m2)
            formeeri(uus_maatriks)
        elif käsk=="-" or käsk.lower()=='lahutamine':
            f1=input("Sisesta esimese maatriksi tekstidokumendi nimi:")
            f2=input("Sisesta teise maatriksi tekstidokumendi nimi:")
            m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
            formeeri(m1)
            print('-')
            formeeri(m2)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=lahuta(m1, m2)
            formeeri(uus_maatriks)
        elif käsk=="*" or käsk.lower()=='korrutamine':
            f1=input("Sisesta esimese maatriksi tekstidokumendi nimi:")
            f2=input("Sisesta teise maatriksi tekstidokumendi nimi:")
            m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
            formeeri(m1)
            print('*')
            formeeri(m2)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=korruta(m1, m2)
            formeeri(uus_maatriks)
        elif käsk.upper()=="D" or käsk.lower()=='determinandi leidmine' or käsk.lower()=='determinant':
            f=input("Sisesta maatriksi tekstidokumendi nimi:")
            m=tagasta_maatriks(f)
            formeeri(m)
            print(25*'-'+'\n'+'Tulemus:')
            determinant=determinant(m)
            print(determinant)
        elif käsk.upper()=="T" or käsk.lower()=='transponeerimine':
            f=input("Sisesta maatriksi tekstidokumendi nimi:")
            m=tagasta_maatriks(f)
            formeeri(m)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=transponeeri(m)
            formeeri(uus_maatriks)
        käsk=input('\n'+"Programmi käsud: +, -, *, D, T või muu sümbol lõpetamiseks: ")

        
    elif sisestamisviis=='käsitsi' or sisestamisviis=='k':
        if käsk=="+" or käsk.lower()=='liitmine':
            print('\t'+'Sisesta esimene maatriks!')
            m1=sisesta_maatriks()
            print('\t'+'Sisesta teine maatriks!')
            m2=sisesta_maatriks()
            formeeri(m1)
            print('+')
            formeeri(m2)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=liida(m1, m2)
            formeeri(uus_maatriks)
        elif käsk=="-" or käsk.lower()=='lahutamine':
            print('\t'+'Sisesta esimene maatriks!')
            m1=sisesta_maatriks()
            print('\t'+'Sisesta teine maatriks!')
            m2=sisesta_maatriks()
            formeeri(m1)
            print('-')
            formeeri(m2)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=lahuta(m1, m2)
            formeeri(uus_maatriks)
        elif käsk=="*" or käsk.lower()=='korrutamine':
            print('\t'+'Sisesta esimene maatriks!')
            m1=sisesta_maatriks()
            print('\t'+'Sisesta teine maatriks')
            m2=sisesta_maatriks()
            formeeri(m1)
            print('*')
            formeeri(m2)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=korruta(m1, m2)
            formeeri(uus_maatriks)
        elif käsk.upper()=="D" or käsk.lower()=='determinandi leidmine'or käsk.lower()=='determinant':
            print('\t'+'Sisesta maatriksi elemendid!')
            m=sisesta_maatriks()
            formeeri(m)
            print(25*'-')
            determinant=determinant(m)
            print(determinant)
        elif käsk.upper()=="T" or käsk.lower()=='transponeerimine':
            print('\t'+'Sisesta maatriksi elemendid!')
            m=sisesta_maatriks()
            formeeri(m)
            print(25*'-'+'\n'+'Tulemus:')
            uus_maatriks=transponeeri(m)
            formeeri(uus_maatriks)
        
        käsk=input('\n'+"Programmi käsud: +, -, *, D, T või muu sümbol lõpetamiseks: ")
