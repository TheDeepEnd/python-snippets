def month_to_num(input):
	input = input.lower()
	if input == "jan" or input == "january":
		return 1
	elif input == "feb" or input == "february":
		return 2
	elif input == "mar" or input == "march":
		return 3
	elif input == "apr" or input == "april":
		return 4
	elif input == "may":
		return 5
	elif input == "jun" or input == "june":
		return 6
	elif input == "jul" or input == "july":
		return 7
	elif input == "aug" or input == "august":
		return 8
	elif input == "sep" or input == "september":
		return 9
	elif input == "oct" or input == "october":
		return 10
	elif input == "nov" or input == "november":
		return 11
	elif input == "dev" or input == "december":
		return 12
	else:
		print input, "== not a valid month"
		return -1

def num_to_month_short(input):
	try:
		input = int(input)
		if input == 1:
			return "jan"
		elif input ==  2:
			return "feb"
		elif input == 3:
			return "mar"
		elif input == 4:
			return "apr"
		elif input == 5:
			return "may"
		elif input == 6:
			return "jun"
		elif input == 7:
			return "jul"
		elif input == 8:
			return "aug"
		elif input == 9:
			return "sep"
		elif input == 10:
			return "oct"
		elif input == 11:
			return "nov"
		elif input == 12:
			return "dec"
		else:
			print input, "== not a valid month!"
			return "INVALID"
	except:
		print "INVALID MONTH"

#TESTS:
print "June:", month_to_num("jun")
print "6:"   , num_to_month_short(6)
