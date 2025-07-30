#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
#The sort() method, changes the order of the list permanently.
# The cars are now in alphabetical order, and we can never revert to
# the original order:

# we can also sort this list in reverse alphabetical order by passing the
# argument reverse=True to the sort() method.
cars.sort(reverse=True)
print(cars)#now this give us the list in reverse alphabatical order.

# Sorting a List Temporarily with the sorted() Function
# The sorted() function lets you display your list
# in a particular order but doesn’t affect the actual order of the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("here is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

# Printing a List in Reverse Order
# The method changes the order of a list permanently  reverse()
# can  be revert to the original order anytime by applyingto the same reverse() list a second time. 
cars.reverse()
print(cars)

#Finding the Length of a List
#You can quickly find the length of a list by using thefunction.len().
print(len(cars))

#Exercise:
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.

fav_loc=["Newzealand","SwitzerLand","Italy","Kashmir","US"]
# Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print(fav_loc)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(fav_loc))

print(fav_loc)#still in original form? YES

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(fav_loc,reverse=True))

print(fav_loc)
#• Use reverse() to change the order of your list. Print the list to show that its order has changed.
fav_loc.reverse()
print(fav_loc)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
fav_loc.reverse()
print(fav_loc)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.f
fav_loc.sort()
print(fav_loc)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
fav_loc.sort(reverse=True)
print(fav_loc)

# 3-11. Intentional Error: If you haven’t received an index error in one of your
# programs yet, try to make one happen. Change an index in one of your programs
# to produce an index error. Make sure you correct the error before closing
# the program.
print(len(fav_loc))
print(fav_loc[5])#list is of 5 element and as it start with 0 index so on printing the location of element at index at 5 it will give us erro
