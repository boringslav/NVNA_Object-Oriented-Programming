months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
newMonths = []

for month in range(len(months)):
    newMonths.append(months[month] * int(month + 1))

for month in newMonths:
    print(month)

