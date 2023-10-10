"""
Chapter 5 Exercise 5: Pets

Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about

each pet
"""
Bay = {"Type of pet":"Dog",
         "Name":"Piolo",
         "Age":"1 year old",
         "Owner":"Bayla"}

Ching = {"Type of pet":"Cat",
         "Name":"Kitty",
         "Age":"9 years old",
         "Owner":"Heleina"}

Doti = {"Type of pet":"Rabbit",
         "Name":"Oreo",
         "Age":"2 years old",
         "Owner":"Dorothy"}

owner=[Bay,Ching,Doti]

for o in owner: 
    print(o) 

