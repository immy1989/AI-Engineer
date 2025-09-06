sales = [1200, 3400, 560, 4500, 2100]

totalSales = sum(sales)
averageSales = totalSales/len(sales)
highSales = max(sales)
lowSales = min(sales)

print(f"Total Sales: {totalSales}")
print(f"Average Sales: {averageSales}")
print(f"Highest Sales: {highSales}")
print(f"Lowest Sales: {lowSales}")