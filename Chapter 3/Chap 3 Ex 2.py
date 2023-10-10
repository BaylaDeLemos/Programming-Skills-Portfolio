"""
Chapter 3 Exercise 2: Greetings
Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
"""
#Lists are used to store multiple items in a single variable.

names = ['Kenalei', 'Cess', 'Yang']
msg="Hello, " + names[0].title()+ "!" + " Kamusta?"
print(msg)

msg = "Hello, " + names[1].title() + "!" + " Kamusta?"
print(msg)

msg = "Hello, " + names[2].title() + "!" + " Kamusta?"
print(msg) 