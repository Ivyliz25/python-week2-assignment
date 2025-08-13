#First we get to create an empty list
my_list = []

#We then go ahead and append the elements which in  this case are 10,20,30,40.

my_list.append("10")
my_list.append("20")
my_list.append("30")
my_list.append("40")
print("My list:", my_list) #Output ['10', '20', '30', '40']

#Let's insert a value(15) at the second position.
my_list.insert(1, "15")
print("My List:", my_list) #Output ['10', '15', '20', '30', '40']

#Let's extend the list by adding more numbers
New_values = ("50", "60", "70")
my_list.extend(New_values)
print("My list:", my_list) #Output ['10', '15', '20', '30', '40', '50', '60', '70']

#Removing the last element we simply pop it out.
my_list.pop(-1)
print("My list:", my_list)

#Arranging in ascending 
Sorted_numbers = sorted(my_list)
print("Sorted Numbers:", Sorted_numbers) #Output ['10', '15', '20', '30', '40', '50', '60', '70']
#or
my_list.sort()
print("My list:", my_list) #Output ['10', '15', '20', '30', '40', '50', '60', '70']

#Let's make things kinds tricky and try sorting them in descending order.
Descending_numbers = sorted(my_list, reverse=True)
print("Descending Numbers:", Descending_numbers) #Output ['70', '60', '50', '40', '30', '20', '15', '10']

#Finally!Let's print the index of 30
#30 in our case is index 3
Number_30 = my_list.index("30")
print("Index:",Number_30) #Output Index:3

#Hurray we're done!!