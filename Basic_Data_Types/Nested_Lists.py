if __name__ == '__main__':
    
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    #Order records with score lower to higher
    records.sort(key=lambda x: x[1])
    lowest_score = records[0][1]
    
    #Obtain the second lower score
    second_lowest = next(score for name, score in records if score > lowest_score)
    
    #Obtain names with the second lower score in alfabetic order    
    second_lowest_names = sorted([name for name, score in records if score == second_lowest])
    print(*second_lowest_names, sep="\n")