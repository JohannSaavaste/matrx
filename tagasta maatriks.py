def tagasta_maatriks(fail):
    f=open(fail, "r")
    jar=[]
    for x in f:
        y=x.strip().split(" ")
        jar.append(y)
    return jar