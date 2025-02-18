if __name__ == '__main__':

    n = int(input())
    #Using list comprehesion  
    print(*[(number+1) for number in range(n)], sep="")
    #Usign a normal loop
    aux=''
    for index in range(n):
        aux += str(index + 1)
    print(aux)

