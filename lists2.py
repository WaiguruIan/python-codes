#Adm NO: BSCIT-05-0096\2024
#Name: Ian Waiguru

names = []
number_of_names = int(input("Enter the number of names you want to enter: ")) 
for i in range (number_of_names):
    
    name = input(f"Enter the name {i+1}: ")
    names.append(name)

names = list(set(names))
names.sort()
print("The sorted names are with no duplicates are:",names)
print ("The total number of names are:",len(names))
