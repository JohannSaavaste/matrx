def ekraanile(maatriks):
    for i in range(len(maatriks)):
        for j in maatriks[i]:
            print(j, end=' ')
        print()
a=[[1, 2, 3],[1, 2, 3]]
b=[['2', '4'], ['6', '8']]
ekraanile(b)