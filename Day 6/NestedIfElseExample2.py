user=input("Please enter the Username: ")
password=input("Please enter the password: ")
if user=='python':
    if password=='welcome':
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")