#overhead cost variables
totalCost = 0
fixedCostPercentage = 10 #TBD
profitMarginPercentage = 40 #TBD
costPerMile = 0.25 #TBD

#costs to add up for total
milageCost = 0
totalFloorCost = 0
installationMethodCost = 0
unitedInches = 0
addOnCost = 0

#floor cost calculation variables
basement = 60
firstFloor = 20
secondFloor = 40
thirdFloor = 60

#install method variables
new_trim_cost = 100
trim_installation_cost = 150
new_stops_cost = 50
stops_installation_cost = 10

#mileage calculation
mileage = input("how many miles is the job from the office? ")
milageCost = int(mileage) * costPerMile

#floor cost calculation
while True:
    floor = input("Basement(0), First(1), Second(2), or Third(3)? ")
    try:
        if int(floor) == 0:
            totalFloorCost += basement
            break
        elif int(floor) == 1:
            totalFloorCost += firstFloor
            break
        elif int(floor) == 2:
            totalFloorCost += secondFloor
            break
        elif int(floor) == 3:
            totalFloorCost += thirdFloor
            break
        else:
            print("basil is SUPER gay ;)")
    except ValueError:
        print("Valid number please")

#install method cost calculation
while True:
    installMethod = input("Full frame(0) or Pocket installation(1)? ")
    # full frame cost
    try:
        if int(installMethod) == 0:
            new_trim = input("New trim (0) or keep existing (1)? ")
            if int(new_trim) == 0:
                installationMethodCost += new_trim_cost + trim_installation_cost
                break
            elif int(new_trim) == 1:
                installationMethodCost += trim_installation_cost
                break
            else:
                print("Invalid Trim selection")
        # pocket install cost
        elif int(installMethod) == 1:
            new_stops = input("New stops (0) or keep existing (1)? ")
            if int(new_stops) == 0:
                installationMethodCost += new_stops_cost + stops_installation_cost
                break
            elif int(new_stops) == 1:
                installationMethodCost += stops_installation_cost
                break
            else:
                print("Invalid Stops selection")
        else:
            print("Invalid Install Type selection")
    except ValueError:
        print("Valid number please")

#United inches calculation
while True:
    try:
        window_width = input("what is the width? ")
        window_height = input("what is the height? ")
        
        united_inches = round(float(window_width) + float(window_height), 2)
    except ValueError:
        print("Valid decimal numbers please")

#window material and style calculation
#TODO: get this from the Manufacturer's API

#add on quesitonaire
addOnInput = input("Are there any additional costs associated with this project? ")
addOnCost = int(addOnInput)

print(f"Your total cost is {totalCost}")

