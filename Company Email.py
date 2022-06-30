name = input("Enter your name: ")
Last_Name = input("Enter your last name: ")
age = input("Enter your age: ")
New_Email = name[0] + Last_Name + "@Company.com"

if age >= 16:
    print("Your email is " + New_Email)
else:
    sign = input("I need an adult signature for your account to be verified, please enter your guardian signature here: ")
    if sign == True:
        print("Your email is " + New_Email)
    else:
        print("Invalid signature, please contact your administrator.")

