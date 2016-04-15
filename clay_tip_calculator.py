
#takes in user input and prints out the tip for the total bsaed on the rate
def calculateTip():
    try:
        total = float(raw_input("Please enter the total amount: "))
        rate  = float(raw_input("Please enter the tax rate (ie .15): "))
    except:
        print "Whoops, please enter a correct value next time!"
        exit()
    tip = total * rate
    print "The tip is: ", tip
    return tip

calculateTip()
