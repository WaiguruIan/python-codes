try:
    result = 10/0
except Exception as e:
    print(f"An error occured: {e}\n")

try :
    result = 50/0
except ZeroDivisionError:
    print(f"Cannot Divide by Zero!!!\n")


try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print ("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
else:
    print("Result: ", result)

finally:# This runs whether there is an error or not so in all of your output will have "Successfully executed"
    print("Succesfully executed")
    print("\n")


def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    print(f"Withdrawn {amount}")

try:
    withdraw(-10)
except ValueError as e:
    print(f"Transaction failed: {e}")