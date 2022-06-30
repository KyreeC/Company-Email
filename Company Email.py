name = input("Enter your name: ")
Last_Name = input("Enter your last name: ")
age = int(input("Enter your age: "))
New_Email = name[0] + Last_Name + "@Company.com"

if age >= 16:
    print("Your email is " + New_Email)
else:
    adult_age = int(input("Enter your guardians age: "))
if adult_age >= 16:
    sign = input("I need an adult signature for your account to be verified, please enter your guardian signature here: ")
else:
    print("Please contact you administrator, your guardian signature will not be accepted")
if sign == True:
    print("Your email is " + New_Email)
else:
    print("Invalid signature, please contact your administrator.")

