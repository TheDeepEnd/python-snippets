
#takes in user input and prints out the tip for the total bsaed on the rate
def calculateTip():
    total = float(input("Please enter the total amount as a float: "))
    rate  = float(input("Please enter the tax rate: "))
    tip = total * rate
    print "The tip is: ", tip 
    return tip

calculateTip()
