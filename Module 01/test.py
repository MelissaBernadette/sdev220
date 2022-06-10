employee = "Bob"
rate = 22.34
hours = float(input("How many hours did " +  employee + " work this week? "))

gross = hours * rate

print(f"{employee} made ${gross:.2f} this pay period.")