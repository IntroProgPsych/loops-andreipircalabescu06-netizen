# https://www.w3schools.com/python/python_for_loops.asp

# Write a program that asks the user for a positive integer n.
# Using a for loop and range(), print all positive integers greater than 0 and smaller than n.
#
# Sample output:
# Upper limit: 5
# 1
# 2
# 3
# 4

def main():
	try:
		n = int(input("Upper limit: "))
	except Exception:
		return
	for i in range(1, n):
		print(i)

if __name__ == "__main__":
	main()

