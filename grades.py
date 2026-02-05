#Adm NO: BSCIT-05-0096\2024
#Name: Ian Waiguru

# Prompt user to enter marks for 3 subjects
# Compute the average 
# Grade the average
subject_1 = int(input("Enter the marks of subject 1: "))
while not (0 <= subject_1 <= 100):
    print("Invalid input! Marks must be between 0 and 100.")
    subject_1 = int(input("Please re-enter the marks of subject 1: "))

subject_2 = int(input("Enter the marks of subject 2: "))
while not (0 <= subject_2 <= 100):
    print("Invalid input! Marks must be between 0 and 100.")
    subject_2 = int(input("Please re-enter the marks of subject 2: "))


subject_3 = int(input("Enter the marks of subject 3: "))
while not (0 <= subject_3 <= 100):
    print("Invalid input! Marks must be between 0 and 100.")
    subject_3 = int(input("Please re-enter the marks of subject 3: "))


total_marks = subject_1 + subject_2 + subject_3
average_marks = total_marks / 3
print(f"The average marks is: {average_marks:.2f}")  # to return at 2 decimal places

if average_marks >= 70:
    grade = "You got grade A"
elif average_marks >= 60:
    grade = "You got grade B"
elif average_marks >= 50:
    grade = "You got grade C"
elif average_marks >= 40:
    grade = "You got a grade D"
else:
    grade = "You got a Fail"

print(grade)

# Write results to a file
f = open("C:\\Users\\Administrator\\Desktop\\Python\\Grades.txt", "w")  # w=write r=read a=append
print("Marks for subject 1: ", subject_1, file=f)
print("Marks for subject 2: ", subject_2, file=f)
print("Marks for subject 3: ", subject_3, file=f)
print("Grade awarded: ", grade, file=f)
f.close()