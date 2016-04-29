import datetime

#Continues to ask the user for input until they submit a valid day
def get_user_month():
    user_month = -1
    while user_month > 12 or user_month < 0:
        try:
            user_month = input("Please enter a valid month (1-12): ")
        except:
            pass
    return user_month

#Continues to ask the user for input until they submit a valid day
def get_user_day():
    user_day = -1
    while user_day > 31 or user_day < 0:
        try:
            user_day = input("Please enter a valid day (1-31): ")
        except:
            pass
    return user_day

#Take in user input
user_month = get_user_month()
user_day = get_user_day()

#Get the current date
now = datetime.datetime.now()

days_elapsed = (int(now.month) * 31) + int(now.day)
target = (int(user_month) * 31) + int(user_day)

todays_date_string = str(now.month) + "/" + str(now.day)
target_date_string = str(user_month) + "/" + str(user_day)

days_till = 0

if target > days_elapsed:
    days_till = target - days_elapsed
else:
    days_till += 365 - days_elapsed
    days_till += target % days_elapsed

print "There are", days_till, "days from", todays_date_string, "to", target_date_string
