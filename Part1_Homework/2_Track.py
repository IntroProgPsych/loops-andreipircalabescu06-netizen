# https://www.w3schools.com/python/python_for_loops.asp
# 
# Write a program that first asks the user how many numbers they will enter.
# Then, using a for loop, read that many integers from the user,
# and at the end print out the LARGEST number entered.
#
# Sample interaction:
# How many numbers? 4
# Number 1: 10
# Number 2: 5
# Number 3: 27
# Number 4: 12
# The largest number was: 27
#
# https://www.w3schools.com/python/python_for_loops.asp
# 
# Write a program that first asks the user how many numbers they will enter.
# Then, using a for loop, read that many integers from the user,
# and at the end print out the LARGEST number entered.
#
# Sample interaction:
# How many numbers? 4
# Number 1: 10
# Number 2: 5
# Number 3: 27
# Number 4: 12
# The largest number was: 27
#
# Hints:
#   - Ask for the count first (how many numbers).
#   - Use a for loop that runs exactly that many times, you can use range(count) for this.
#   - Keep track of the current maximum in a variable.
#   - Update the maximum whenever you read a number that is larger.

# Write your code here:

def main():
	try:
		count = int(input("How many numbers? "))
	except Exception:
		return

	max_num = None
	for i in range(1, count + 1):
		try:
			n = int(input(f"Number {i}: "))
		except Exception:
			# if invalid input, skip this iteration
			continue
		if (max_num is None) or (n > max_num):
			max_num = n

	if max_num is None:
		# No valid numbers were entered; print a default
		print("The largest number was: 0")
	else:
		print(f"The largest number was: {max_num}")


if __name__ == "__main__":
	main()
