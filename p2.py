print("program to find whether the given integer is positive or negative")

print ("*"* 75)

number = int(input("Enter an integer: "))

while number == 0:
	print("Zero")
	break
else:
	if number > 0:
		print("Positive")
	elif number < 0:
		print("Negative")
