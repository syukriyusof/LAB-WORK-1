"""
 Program Purpose: To ask user to input data and calculate the exchange rates of Malaysian Ringgit to other country currencies based on the global current rates.
 Programmer: MUHAMMAD SYUKRI BIN MHD YUSOF (AM2307013981)
 Date: 7 February 2024
"""

#Prompt the user to choose the types of exchange rates
print("Currency Conversion Program")
print() #blank line
print("Exchange Rates:")
print("USD - US Dollar: 0.25")
print("EUR - Euro: 0.21")
print("GBP - British Pound: 0.18")
print() #blank line
print("Choose the target currency:")
print("1. USD - US Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound")
print() #blank line
#Input from the user will be be assigned in the variable named choice
choice = int(input("Enter your choice (1 or 2 or 3) based on the given options: "))

if choice == 1: #To calculate the exchange rates of Malaysian Ringgit to US Dollar
    malaysian_ringgit = float(input("Enter the amount in Malaysian Ringgit: "))
    equivalentAmount = malaysian_ringgit * 0.25
    print("The equivalent amount in US Dollar (USD) is : ", equivalentAmount)
elif choice == 2:
    malaysian_ringgit = float(input("Enter the amount in Malaysian Ringgit: "))
    equivalentAmount = malaysian_ringgit * 0.21
    print("The equivalent amount in Euro (EUR) is : ", equivalentAmount)
elif choice == 3:
    malaysian_ringgit = float(input("Enter the amount in Malaysian Ringgit: "))
    equivalentAmount = malaysian_ringgit * 0.18
    print("The equivalent amount in British Pound (GBP) is : ", equivalentAmount)

else:
    print("Invalid option! Please re-enter choices given")