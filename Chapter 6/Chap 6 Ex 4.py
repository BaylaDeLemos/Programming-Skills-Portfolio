"""
Chapter 6 Exercise 4: Deli

Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
"""
sandwich_order=["Grilled Cheese Sandwich","Egg Sandwich","Tuna Sandwich"]
finished_sandwiches=[]
while sandwich_order:
    sandwich=sandwich_order.pop() 
    print("I'm making your",sandwich)
    finished_sandwiches.append(sandwich)
print("\n")
for fs in finished_sandwiches: 
    print("I'm finished making your",fs)
    