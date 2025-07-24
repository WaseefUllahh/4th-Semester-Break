bicycles=["yamaha","honda","suzuki","kawasaki"]
print(bicycles[0])
#I initialized a list bicycles and i have printed the first index by bicycle[0] as the list in python starts from zero.

print(bicycles[0].title())#now it will print it in more professional manner beccause of title fuunction on string.

#by asking for index at -1 python returns the last element of the list.
print(bicycles[-1].title())#just like this -2 and -3 will return 2nd last and 3rd last element of the list.

# we can use f-strings to create a message based on a value from a list.
print(f"My first Bicycle was {bicycles[1].title()}")

# Exercises:
# Store the names of a few of your friends in a list called names,Print
# each person’s name by accessing each element in the list, one at a time.

friend_names=["Rehan khan","Wajahat Ullah","Usama Burki","Umar Shehzad"]
print(f"My best friend is {friend_names[0]} and {friend_names[1]} .")

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

print(f"My best friend are also  {friend_names[2]} and {friend_names[3]} .")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

motorcycle_list=["Honda","Kawasaki","Yamaha"]
print(f"I would like to own a {motorcycle_list[1]} ninja h2r one day.")

motorcycle_list.append("Ducati")#append function is used to add something to the ennd of the list.



motorcycle_list.insert(0,"ninjaYBR")#insert function used in list for adding an element at a specific index 
#mong ba warth pela index ao by element nom ba mention kao che km zai ba sa element kedei pa list kei ao nor element ba shift shei right la
print(motorcycle_list)


#If I know the position of the item we want to remove from a list, we can use the del statement.
del motorcycle_list[0]
print(motorcycle_list)


# pop function use with list to remove last element from the list but we can also store it in a variable for further use.
poped_bike=motorcycle_list.pop()
print(poped_bike)
poped_bike=motorcycle_list.pop()
print(poped_bike)

print(motorcycle_list)
motorcycle_list.append("HONDA 125")
motorcycle_list.append("Unique 70")

# Popping Items from any Position in a List
# we can use pop() to remove an item from any position in a list by including
# the index of the item you want to remove in parentheses.when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an
# item as you remove it, use the pop() method.

print(motorcycle_list)

motorcycle_list.pop(2)#we can pop any element with known index using the index inside pop.
print(motorcycle_list)

# Removing an Item by Value
# say we want to remove the value 'Kawasaki' from the list of
# motorcycles.we will use remove function when we know the element value we want to remove.

motorcycle_list.remove('Kawasaki')
print(motorcycle_list)

# EXERCISES
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guests=["Zulqarnain","Quaid-e-Azam","Waseef Ullah"]
print(f"{guests[0]} Peace be upon you it my heartly wish to invite you to dinner and talk to you for long time")
print(f"{guests[1]} i want to  invite you to dinner and talk to you for long time")
print(f"I wnant to invite {guests[2]} to dinner and talk to you for long time")

print(f"{guests[1]} can't make it due to important meetings")

guests[1]="Khalid bin Waleed"
print(f"{guests[1]} i want to  invite you to dinner and talk to you for long time")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

print(f"{guests[0]} {guests[1]} and {guests[2]} I just found a new and bigger table.")
guests.insert(0,"Ghaznawi")
guests.insert(2,"Taipu Sultan")
guests.append("ALI(RA)")

print(f"{guests[0]} {guests[1]} and {guests[2]} {guests[3]} {guests[4]} and {guests[5]}.")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

print("Oh no I can invite only two personnns...........")

popped_person=guests.pop()
print(f"{popped_person} I am sorry that i cant invite you to dinner.")
popped_person=guests.pop()
print(f"{popped_person} I am sorry! that i cant invite you to dinner.")
popped_person=guests.pop()
print(f"{popped_person} I am sorry that i cant invite you to dinner.")
popped_person=guests.pop()
print(f"{popped_person} I am sorry that i cant invite you to dinner.")

print(f"{guests[0]} {guests[1]}  you are still invited.")
del guests[0]
del guests[0]
print(guests)

