if __name__ == '__main__':

    n = int(input())
    
    #List comprehesion
    print(*[index**2 for index in range(n) ], sep="\n")
    #Normal loop for
    for index in range(n):
        print(index**2)

