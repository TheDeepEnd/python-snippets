#method that takes in user input and prints out the tip for the total based on the rate
def calculateTip():
    try:
	#ask user for input
        total = float(raw_input("Please enter the total amount: "))
        rate  = float(raw_input("Please enter the tax rate (ie .15): "))
    except:
	#the user has entered an invalid value
        print "Whoops, please enter a correct value next time!"
        exit()
    #calculate tip
    tip = total * rate

    #print tip
    print "The tip is: ", tip
    return tip

#call method
calculateTip()
