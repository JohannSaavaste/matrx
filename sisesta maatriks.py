def sisesta_maatriks():
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
print(sisesta_maatriks())