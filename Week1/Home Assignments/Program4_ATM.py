inputAmount = int(input("Enter Withdrawal Amount:"))

if(inputAmount%100 == 0):
    print(f"Dispensing {inputAmount}")
else:
    print("Invalid Amount")