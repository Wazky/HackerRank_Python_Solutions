def count_substring(string, sub_string):
    occurrences = 0
    for i in range(0, (len(string) - len(sub_string) + 1)):
        if (string[i:(len(sub_string) + i)] == sub_string):
            occurrences += 1
    return occurrences

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)