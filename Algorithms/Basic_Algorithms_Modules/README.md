# Basic_Algorithms_Modules

In this unit you will begin exploring simple ```algorithms``` which allow us to solve problems by breaking them into steps.

Each of the Algorithms we go over can be used with a ```list``` of data - preferably numbers - to achieve some outcome!

Key Terms & Vocab:
1. **Algorithm** - A set of steps to solve a problem
2. **List** - a python data type that contains a list of other data
3. **Len** - the len(my_list) command allows you to retrieve the number of items in a list. For example: if ```my_list = [1,2,3]``` then ```len(my_list)``` is 3 since there are 3 items in the list.
4. **For Loop** - a loop that executes a segment of code *for each* item in a list (i.e. for each fruit in the list of fruits, add to the fruit tally to count how many fruits there are)
   Syntax -
   ```
   for variable_name in my_list:
     print("Any code indented down here will execute for each item in my_list")
   ```
6. **Index** - The "location" in a list. Lists start at index 0 and count up. For example: ```[1,2,3,4,5]``` - this list contains '1' at index 0 and '5' at index 4. 
7. **List Traversals** - A fancy name for a while loop or for loop that walks through a list. like ```for i in range(10):``` which would execute the following code 10 times.
8. **Modulo - %** - The % operator checks for a remainder if two numbers are divided. For example: ```12 % 2 = 0``` since 12 is evenly divisible by 2 there is no remainder, our answer is 0.
9. **Average** - The "middle" most part of a list. By taking the sum of all numbers, then dividing by the count of numbers, you can find the 'average' number. For example: ```average = sum(numbers) / len(numbers)```


Algorithms (and what they do):
1. Divisibility - Checks to see if two numbers are evenly divisible.
2. Sum - Adds up a *list* of numbers.
3. Min/Max - Find the biggest/smallest out of a list.
4. Linear Search - Finds a target in a list by searching item by item.
5. Binary Search - Finds a target in a *sorted* list by splitting the search area in half each step.

algorithms.py contains a toolkit of functions that can be imported for the final project or to test out functions we create in the lessons!
