def leia_det(m, n):
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
def determinant(maatriks):
    if len(maatriks)==len(maatriks[0]):
        return leia_det(maatriks, len(maatriks))
    else:
        return "Maatriksist ei saa determinanti leida."
print(determinant([['3', '5', '7', '3'], ['1', '5', '2', '5'], ['1', '5', '7', '8'], ['1', '4', '6', '2']]))           