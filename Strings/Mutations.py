def mutate_string(string, position, character):
    #Converting String to list and modify it
    '''
    l = list(string)
    l[position] = character
    return ''.join(l)
    '''
    #Using string slicing
    return string[:(position)] + character + string[(position+1):]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)