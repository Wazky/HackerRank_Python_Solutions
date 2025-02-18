if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    li = list(arr)
    #Generate a list without the max values instances and find the new max
    print(max([i for i in li if i != max(li)]))