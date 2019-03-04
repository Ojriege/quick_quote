window_price = 0
new_trim_cost = 100
trim_installation_cost = 150
new_stops_cost = 50
stops_installation_cost = 10


while True:
    floor = input("Basement(0), First(1), Second(2), or Third(3)?")
    try:
        if int(floor) == 0:
            window_price += 60
            break
        elif int(floor) == 1:
            window_price += 20
            break
        elif int(floor) == 2:
            window_price += 40
            break
        elif int(floor) == 3:
            window_price += 60
            break
        else:
            print("basil is gay")
    except ValueError:
        print("Valid number please")


installType = input("Full frame(0) or Pocket installation(1)?")
# full frame
if int(installType) == 0:
    new_trim = input("New trim (0) or keep existing (1)")
    if int(new_trim) == 0:
        window_price += new_trim_cost + trim_installation_cost
    elif int(new_trim) == 1:
        window_price += trim_installation_cost
    else:
        print("Invalid Trim selection")
# pocket install
elif int(installType) == 1:
    new_stops = input("New stops (0) or keep existing (1)")
    if int(new_stops) == 0:
        window_price += new_stops_cost + stops_installation_cost
    elif int(new_stops) == 1:
        window_price += stops_installation_cost
    else:
        print("Invalid Stops selection")
else:
    print("Invalid Install Type selection")

print(f"Your total cost is {window_price}")

window_width = input("what is the width?")
window_height = input("what is the height?")

united_inches = round(float(window_width) + float(window_height), 2)


windowStyle = input("""What style of window do you need? 
             -Vinyl(0) -Wood(1) -Fiberglass(2)""")

windowType = input("""What is the style of the window?
                   -Sliding(0) -Fixed(1) -Casement(2) -DoubleHung(3) -SingleHung(4) """)
