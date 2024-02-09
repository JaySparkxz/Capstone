import csv
import math 

TotalQuestions = 0
Goal = .75
WrongAnswers = 0
CorrectAnswers = 0    

with open('./QSHort.csv', newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader: 
        TotalQuestions += 1
MaxWrongAnswers = math.ceil(TotalQuestions-(TotalQuestions*Goal))
        
with open('./QSHort.csv', newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    print(f'MaxWrongAnswers: {MaxWrongAnswers}')
    for row in reader:
        if MaxWrongAnswers > WrongAnswers:
            answer = int(input(f"{row['Num1']} + {row['Num2']} = "))
            if int(answer) == int(row['Answer']):
                CorrectAnswers += 1
            else:
                WrongAnswers += 1
        else:
            print("The maximum number of wrong answers has been reached, try again later.")
            break
        
