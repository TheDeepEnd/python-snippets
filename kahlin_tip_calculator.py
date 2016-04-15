# Asks for price, if it isn't a number asks again
while True:
    try:
        cost = float(raw_input("What is the cost of your meal? $"))
        break
    except ValueError:
        print("Please enter a monetary value.")


# Asks for tax and then figures out said tax, if it isn't a number asks again        
while True:
    try:
        tax = float(raw_input("What is the tax rate in your state? If it is a whole number such as '15' please enter it as 15.0. "))
        tax = tax/100
        break
    except ValueError:
        print("A tax has to be a number...")


# Asks for tip and figures out said tip, if it isn't a number asks again        
while True:
    try:
        tip = float(raw_input("What would you like to tip? If it is a whole number such as '15' please enter it as 15.0. "))
        tip = tip/100
        break
    except ValueError:
        print("This is the third step in paying your bill yet you still fuck it up. Enter a number.")

# Sets cost and total to the appropriate values
cost = cost + cost*tax       
total = cost + cost*tip

# Prints out the total using the % operator to fill in the place holder
print "Your total is $%s. Thank you for eating at Kahlin's House, please pay Tor on the way out." % (total)