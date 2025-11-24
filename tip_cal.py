"""
To calculate the tip per person based on total bill the amount of tip the used need to pay
"""


a=int(input("Enter the total bill:"))
b=int(input("Enter the tip percentage:"))
n=int(input("Enter number of people:"))
tip=(a*(b/100)+ a)/n
print("Each person should pay: ", tip)
