# https://www.w3schools.com/python/python_while_loops.asp

#  You are given this dictionary:
# translations = {
#     "cat": "pisică",
#     "dog": "câine",
#     "red": "roșu",
#     "sun": "soare"
# }
#
# Write a program that:
#   1. Uses a while loop to repeatedly ask the user for an English word.
#   2. If the user types "exit", stop the loop.
#   3. If the word exists in the dictionary, print the Romanian translation.
#   4. Otherwise, print "Word not found".
#
# Sample interaction:
# Word: cat
# pisică
# Word: tree
# Word not found
# Word: dog
# câine
# Word: exit
# Goodbye!
#
# Requirements:
#   - use a while loop
#   - use the dictionary for lookup
#   - stop only when the user types "exit"

# Write your code here:
translations = {
    "cat": "pisică",
    "dog": "câine",
    "red": "roșu",
    "sun": "soare"
}

def main():
    while True:
        word = input("Word: ")
        if word == "exit":
            print("Goodbye!")
            break
        if word in translations:
            print(translations[word])
        else:
            print("Word not found")


if __name__ == "__main__":
    main()

