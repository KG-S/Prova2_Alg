#ex 2 prova

def cor(lista):
    esque = 0
    dire = 0
    listaZero = []
    listaLapis = []
    
    for i in range(len(lista)):
        if lista[i] == 0:
            listaZero.append(i)




    for i in range(len(lista)):
        esque = 0
        dire = 0
        if lista[i] != 0:
            if i < listaZero[0]:
                listaLapis.append(listaZero[0]-i)
            elif i > listaZero[-1]:
                listaLapis.append(i-listaZero[0])
            else:
                for o in range(len(listaZero)):
                    if i > listaZero[o]:
                        if i < listaZero[o+1]:
                            if esque > (listaZero[o] - i):
                                esque = listaZero[o] - i
                            if dire > (i - listaZero[o+1]):
                                dire = i - listaZero[o+1]

                            
                    if i < listaZero[o]:  
                        if i > listaZero[o-1]:
                            if esque > (i -listaZero[o] - i):
                                esque = listaZero[o] - i
                            if dire > (i - listaZero[o+1]):
                                dire = i - listaZero[o+1]
                        
                    print(lista[i],i, o, esque, dire)



                    

               
                     




lapis = [-1,0,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1, 0, -1]
cor(lapis)