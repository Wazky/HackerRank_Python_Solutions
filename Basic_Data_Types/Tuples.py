if __name__ == '__main__':
    
    n = int(input())
    integer_list = map(int, input().split())
    #Generate the tuple from the map
    t = tuple(integer_list)
    #Create a hash from the tuple and print it
    print(hash(t))