# this file contains code from the group project writeup, and extra examples of how to use different types of loops to reverse strings

# counting while loop
i = 0
while i < 10:
    i += 1
print(i)

# counting for loop
for i in range(3):
    print(i)

# using a for loop to repeatedly run a print statement
for i in range(3):
    print("Hello For Loop")

# using a while loop to repeatedly run a print statement
i = 0
while i < 3:
    print("Hello While Loop")
    i += 1

# using a while loop to reverse a string
string_while = "Hello While"
reversed_while = ""
i = 0
while i < len(string_while):
    reversed_while = string_while[i] + reversed_while
    i += 1
print(reversed_while)

# using a for loop with range to reverse a string
string_for = "Hello For"
reversed_for = ""
for i in range(len(string_for)):
    reversed_for = string_for[i] + reversed_for
print(reversed_for)

# neither of these are quite optimal, but accomplish the same task

