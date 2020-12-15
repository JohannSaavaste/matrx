def korruta(m1,m2):
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
print(korruta([['2', '3', '5', '8'], ['1', '2', '5', '7'], ['5', '7', '2', '8']], [['3', '5', '7', '3'], ['1', '5', '2', '5'], ['1', '5', '7', '8'], ['1', '4', '6', '2']]))