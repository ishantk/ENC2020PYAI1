"""

    COVID-19 use Case
    Search, Sort and Filter Operations on Data

"""

# MODEL
state1 = {
    "active": 881,
	"confirmed": 3497,
	"deaths": 78,
	"recovered": 2538,
	"state": "Punjab",
}

state2 = {
    "active": 51922,
	"confirmed": 116752,
	"deaths": 5651,
	"recovered": 59166,
	"state": "Maharashtra",
}

state3 = {
	"active": 21993,
	"confirmed": 50193,
	"deaths": 576,
	"recovered": 27624,
	"state": "Tamil Nadu",
}

state4 = {
	"active": 27741,
	"confirmed": 47102,
	"deaths": 1904,
	"recovered": 17457,
	"state": "Delhi",
}


state5 = {
	"active": 6149,
	"confirmed": 25148,
	"deaths": 1561,
	"recovered": 17438,
	"state": "Gujarat",
}

state6 = {
	"active": 5659,
	"confirmed": 15785,
	"deaths": 488,
	"recovered": 9638,
	"state": "Uttar Pradesh",
}

state7 = {
	"active": 2721,
	"confirmed": 13626,
	"deaths": 323,
	"recovered": 10582,
	"state": "Rajasthan",
}

state8 = {
	"active": 2308,
	"confirmed": 11426,
	"deaths": 486,
	"recovered": 8632,
	"state": "Madhya Pradesh",
}

state9 = {
	"active": 4528,
	"confirmed": 7944,
	"deaths": 134,
	"recovered": 4983,
	"state": "Haryana",
}

state10 = {
	"active": 2842,
	"confirmed": 3615,
	"deaths": 115,
	"recovered": 2570,
	"state": "Karnataka",
}

indian_states = [state1, state2, state3, state4, state5, state6, state7, state8, state9, state10]

# VIEW
print("++++++++++++++++++COVID19 India++++++++++++++++++++")

print("Press 1 for Filtering COVID-19 Data using 2 Filters")
print("Press 2 Search Data By State")
print("Press 3 for sorting Cases with 1 Filter")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++")

choice = int(input("Enter Your Choice:"))


# CONTROLLER
if choice == 1:
	# FILTERING
    filter1 = input("Please choose 1st filter from [active | confirmed | deaths | recovered | state}] : ")
    filter2 = input("Please choose 2nd filter from [active | confirmed | deaths | recovered | state}] : ")

    for i in range(len(indian_states)):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{}: {}\n{}: {}".format(filter1, indian_states[i][filter1], filter2, indian_states[i][filter2]))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

elif choice == 2:
	# SEARCH
	state = input("Enter the State to Search:")
	for i in range(len(indian_states)):
		if state.lower() == indian_states[i]["state"].lower():
			print("State Found:", state.upper())
			print(indian_states[i])
			break

elif choice == 3:
    # SORT
	sort_filter = input("Please choose filter from [active | confirmed | deaths | recovered}] : ")
	n = len(indian_states)

	for i in range(0, n):
		for j in range(0, n - i - 1):
			if indian_states[j][sort_filter] > indian_states[j + 1][sort_filter]:
				# swap the elements
				indian_states[j], indian_states[j + 1] = indian_states[j + 1], indian_states[j]

	for i in range(0, n):
		print(indian_states[i])
		print("~~~~~~~~~~~~~~~")
else:
    print("INVALID CHOICE")