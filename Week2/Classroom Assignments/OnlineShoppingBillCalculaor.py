# Function to calculate total bill
def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total

# Different ways to call the function

# 1. Only positional arguments
print("Bill 1:", calculate_bill(500, 2)) 

# 2. Positional arguments + custom tax
print("Bill 2:", calculate_bill(500, 2, tax=0.1))  

# 3. Positional arguments + custom discount
print("Bill 3:", calculate_bill(500, 2, discount=50))  

# 4. Positional arguments + custom tax and discount
print("Bill 4:", calculate_bill(500, 2, tax=0.08, discount=100))  
