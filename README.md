# python-week2-assignment
This Python script demonstrates various list operations including creation, appending, inserting, extending, removing, sorting, and finding indexes.

Operations Demonstrated
List Creation

Initializes an empty list my_list

Appending Elements

Adds elements "10", "20", "30", "40" to the list

Output: ['10', '20', '30', '40']

Inserting Elements

Inserts "15" at the second position (index 1)

Output: ['10', '15', '20', '30', '40']

Extending the List

Adds new values "50", "60", "70" from a tuple

Output: ['10', '15', '20', '30', '40', '50', '60', '70']

Removing Elements

Removes the last element using pop(-1)

Output: ['10', '15', '20', '30', '40', '50', '60']

Sorting Operations

Ascending sort using sorted() and sort()

Descending sort using sorted(reverse=True)

Finding Index

Locates the index of value "30" (output: 3)

Usage
Run the script directly with Python:

bash
python list_operations.py
The script will execute sequentially and print outputs after each operation.

Notes
All values are stored as strings (note the quotation marks)

The script demonstrates both sorted() (creates new list) and sort() (in-place) methods

Includes both ascending and descending sort examples

Expected Output
text
My list: ['10', '20', '30', '40']
My List: ['10', '15', '20', '30', '40']
My list: ['10', '15', '20', '30', '40', '50', '60', '70']
My list: ['10', '15', '20', '30', '40', '50', '60']
Sorted Numbers: ['10', '15', '20', '30', '40', '50', '60']
My list: ['10', '15', '20', '30', '40', '50', '60']
Descending Numbers: ['60', '50', '40', '30', '20', '15', '10']
Index: 3
