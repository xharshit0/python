x = int(input("Enter the citizen age-"))

if  (x <= 12):
    print("Citizen is a kid")
elif (x>12)and(x<=20):
    print("Citizen is a teenager")
elif(x>=19)and(x<=60):
    print("Citizen is a adult")
else:
    print("Citizen is a old person")
    