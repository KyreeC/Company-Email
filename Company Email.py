import random

name = input("Enter your first name: ")
Last_Name = input("Enter your last name: ")
age = int(input("Enter your age: "))


New_Email = name[0] + Last_Name + "@Company.com"

if age >= 16:
    print("Your email is: " + New_Email)
    print("Your company ID is: " + str(random.randint(100000, 999999)))
else:
    adult_age = int(input("Enter your guardians age: "))
        
    try:  # The logic in the "try" block below only gets evaluated if the "else" statement above gets triggered.
        if adult_age >= 16:
            signature = input("I need an adult signature for your account to be verified, please enter your guardian signature here: ")

            if signature != "":  # Checks to make sure the signature is not empty.
                print("Your email is: " + New_Email)
                print("Your company ID is: " + str(random.randint(100000, 999999)))
            else:
                print("Invalid signature, please contact your administrator.")

        else:
            print("Please contact you administrator, your guardian signature will not be accepted")

    except NameError as e:
        print(f"There was an error: {e}\nTry again.")