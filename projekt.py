kask=input("Programmi käsud: +, -, *, D, T")
if kask=="+":
    f1=input("Sisesta esimese maatriksi tekstidokumendi nimi:")
    f2=input("Sisesta teise maatriksi tekstidokumendi nimi:")
    m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
    uus_maatriks=liida(m1, m2)
elif kask=="-":
    f1=input("Sisesta esimese maatriksi tekstidokumendi nimi:")
    f2=input("Sisesta teise maatriksi tekstidokumendi nimi:")
    m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
    uus_maatriks=lahuta(m1, m2)
elif kask=="*":
    f1=input("Sisesta esimese maatriksi tekstidokumendi nimi:")
    f2=input("Sisesta teise maatriksi tekstidokumendi nimi:")
    m1,m2=tagasta_maatriks(f1), tagasta_maatriks(f2)
    uus_maatriks=korruta(m1, m2)
elif kask=="D":
    f=input("Sisesta maatriksi tekstidokumendi nimi:")
    m=tagasta_maatriks(f)
    determinant=determinant(m)
elif kask=="T":
    f=input("Sisesta maatriksi tekstidokumendi nimi:")
    m=tagasta_maatriks(f)
    uus_maatriks=transponeeri(m)
