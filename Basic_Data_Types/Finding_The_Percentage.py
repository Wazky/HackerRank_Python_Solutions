def getAverage(student_name, student_marks):
    #Check if student in dictionary
    if student_name in student_marks:
        #Average = Sum marks / marks of the student
        return sum(student_marks[student_name])/len(student_marks[student_name])
    else:
        print("Student isn't in the dictionary")

if __name__ == '__main__':
    
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #Get the student name to get the average
    query_name = input()
    #Print the average with 2 decimal precision
    print(f"{getAverage(query_name, student_marks):.2f}")
    