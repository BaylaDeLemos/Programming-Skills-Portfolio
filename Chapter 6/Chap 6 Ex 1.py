"""
Chapter 6 Exercise 1: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""
while True: 
    pt=input("Please enter your topping/s:")
    print("We will add", pt,"to your pizza")
    if pt=="quit":
        print("Thank you for odering")
        break