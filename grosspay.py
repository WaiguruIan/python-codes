#Adm NO: BSCIT-05-0096/2024
#Name: Ian Waiguru

Hours = int(input("Enter the hours: "))
Rate = float(input("Enter the rate: "))
Gross_pay = Hours * Rate

print("The hours are ", Hours)
print("The rate is ", Rate)
print("The gross pay is ", Gross_pay)


f = open ("C:\\Users\\Administrator\\Desktop\\Python\\gross.txt", "w")#w=write r=read a=append
print ("Hours: ", Hours, file=f)
print("Rate: ", Rate , file=f)
print("Gross pay: ", Gross_pay, file=f)
f.close()

