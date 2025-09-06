employees = ["John", "Patrick", "Jane", "Lara", "Stokes"]

#for emp in employees:
#    print(emp)

for index, emp in enumerate(employees, 1):
    print(f"{index}. {emp}")