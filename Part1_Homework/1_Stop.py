# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_while_loops.asp

# Write a program that asks the user for a target number.
# Using a while loop, repeatedly ask the user for numbers and keep
# adding them to a running total.
#
# The loop should stop when the total reaches or exceeds the target.
# After the loop ends, print the final total.
#
# Sample interaction:
# Target: 20
# Number: 5
# Number: 7
# Number: 4
# Number: 10
# Total reached: 26
#
# Hints:
#   - Ask for the target once (outside the loop)
#   - Start a variable total = 0
#   - In each iteration, ask for a new number and add it to total
#   - Stop only when total >= target

# Write your code here:

def main():
	try:
		target = int(input("Target: "))
	except Exception:
		return

	total = 0
	while total < target:
		try:
			n = int(input("Number: "))
		except Exception:
			continue
		total += n

	print(f"Total reached: {total}")


if __name__ == "__main__":
	main()
