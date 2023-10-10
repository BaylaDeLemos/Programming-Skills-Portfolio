"""
Chapter 2 Exercise 5: USB Shopper
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programe that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise. 
"""
#An Arithmetic Operator is a mathematical function that performs a calculation on two operands.

a=50
b=6
c=int(a/b)
print("The girl can get", c , "pieces of USB sticks\n")

a1=50
b1=6
c1=int(b1*c)
d1=round(float(a-c1), 2)
print("The girl will have" , d1 ,'left')