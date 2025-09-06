correctPassword = "openAI123"

for i in range(3):
    inputPassword = input("Enter the password:")

    if(inputPassword == correctPassword):
        print("Login Successful")
        break
else:
    print("Account Locked")
        
