"""
Chapter 2 Exercise 3:  Stripping Names
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""
#Use the .strip() method to remove whitespace and characters from the beginning and the end of a string. 
#Use the .lstrip() method to remove whitespace and characters only from the beginning of a string. 
#Use the .rstrip() method to remove whitespace and characters only from the end of a string.

name = "\tBayla De Lemos\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

