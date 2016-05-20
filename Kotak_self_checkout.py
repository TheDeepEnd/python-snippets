'''
    1) Add an item to your cart
    2) Proceed to checkout
    3) Quit
    $ 1
    Enter item description: Red Bull
    Enter item quantity: 48
    Price per unit: $2.00
    $ 2
    48 - Red Bull @ $2.00 ea
    Subtotal: $96.00
    Tax (4.712%): $4.52
    Total: $100.52

age =  raw_input("How old is you? ")
height = raw_input("How tall is u? ")
weight = raw_input("How much mass is u? ")

print 'so youz %r old, %r tall, and %r heavy.'\
%(age, height, weight)
'''
menu = ['Checkout', 'Hershey\'s Chocolate Bar', \
'Red Bull Energy Drink', 'Monster Energy Drink']

prices = [' ', 1.00, 2.00, 2.00]

cart = []
def Menu():
    count = 0
    print("Below is the menu, enter the number corresponding to\
the item you would like, 0 is to checkout")
    print("0. Checkout")
    print("1. Hershey\'s Chocolate Bar $1.00")
    print("2. Red Bull Energy Drink $2.00")
    print("3. Monster Energy Drink $2.00")
    item = raw_input("> ")
    try:
        if int(item) == 0:
            Checkout();
        elif int(item) <= 3 and int(item) != 0:
            cart.append(item)
            count = count + 1
            print("Please specify a quantity of the item you would like ")
            qty = raw_input("> ")
            cart.append(qty)
            count = count + 1
            print(cart[count-1])
            Menu()
        else:
            print "Please specify a number that is in our menu."
    except ValueError as e:
        print("Please enter an integer.")
        Menu()
def Checkout():
    total = 0.0
    for i in range(0,len(cart)):
        if i == 0:
            continue
        # print(cart[i])
        print("You have ordered %s %s" %(cart[i-1], menu[i]))
        total = prices[i] + total
    print("Your total is $%s" %(total))
if __name__ == '__main__':
    Menu()
