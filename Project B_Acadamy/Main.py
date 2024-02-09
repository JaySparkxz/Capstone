import csv
import math 


# ===== variables ======
TotalQuestions = 0
Goal = .75
WrongAnswers = 0
CorrectAnswers = 0    
# ===== =====


# Opens a csv file with questions and answers. Currently set up to add two numbers in two seperate columns 
with open('./QSHort.csv', newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader: 
        TotalQuestions += 1

# Calcs Maxiomum number of wrong answers 
MaxWrongAnswers = math.ceil(TotalQuestions-(TotalQuestions*Goal))

        
with open('./QSHort.csv', newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    
    # print(f'MaxWrongAnswers: {MaxWrongAnswers}') Check to make sure MaxWrongAnswers is an int. 
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
        
