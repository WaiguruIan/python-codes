#Adm NO: BSCIT-05-0096\2024
#Name: Ian Waiguru

#decision making
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
if (years_of_service > 10):
    bonus = 0.1 * salary
elif (years_of_service >=6 and years_of_service <=10):#no && for and
    bonus = 0.08 * salary
else:
    bonus = 0.06 * salary

print("The bonus allocated is: ",bonus)

net_salary = bonus + salary
print("The net salary is: ",net_salary)

#This is used to create a .txt file named "bonus.txt" that would have the following fields
#write w is used to overwrite existing data in the .txt file
#append a is used to add data under an existing data
f = open ("C:\\Users\\Administrator\\Desktop\\Python\\bonus.txt", "w")#w=write r=read a=append
print ("Salary ", salary, file=f)
print("Years of service: ", years_of_service , file=f)
print("Bonus awarded ", bonus, file=f)
print("The net salary: ", net_salary, file=f)
f.close()


   
