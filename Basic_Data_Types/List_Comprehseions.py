if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    #Create all permutations
    permutations = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    #Filter ones which sum != n
    permutations_underN = [element for element in permutations if sum(element) != n]
    print(permutations_underN)

    #Same but in one code line
    print( [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
