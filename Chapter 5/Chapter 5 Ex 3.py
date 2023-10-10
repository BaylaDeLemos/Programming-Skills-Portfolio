"""
Chapter 5 Exercise 3: Glossary 2 

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""
glossary = {
   'loop': 'Work through a collection of items, one at a time.',
   'list': 'A collection of items in a particular order.',
   'print': 'is used to send message or output to the screen.',
    'strings': 'are text enclosed in single or double quotes.',
    'boolean': 'can be represented as true or false.',
    'float': 'A numerical value with a decimal component.',
    'integers': 'whole number datas.',
    'operator': 'A special symbol that represents a simple computation',
    'variable': 'A variable is a location that stores temporary data within a program.',
    'input':  'Input refers to the information that goes into the computer'
    }
for g in glossary:
    print(g, ":",glossary[g]) 