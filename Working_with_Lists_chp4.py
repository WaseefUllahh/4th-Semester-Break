#FOR LOOP

cats=["irani","islamabadi","blackie"]#good examples of using for loop : for cat in cats:, for dog in dogs: ,for item in list_of_items:
print("MY CATS:")
for cat in cats:
    print("\t",cat,"\n")


magicians = ['Hamad', 'sunil', 'Waseef']# A list for magiicians.
for magician in magicians:#we define a for loop. This line tells Python to pull a name from the list magicians, and associate it with the variable magician.
    print(magician)#For every magician in the list of magicians, print the magician’s name.
    print(f"{magician.title()} that was a great trick btw not gonna lie. You are good at what you do....")
    print(f"can't wait to see your next magic trick {magician.title()}!.........\n")

#Doing Something After a for Loop
print(f"*****...Thank you {magicians} that was a great show*****...\n")#this line is not intended so it will print only one time.

#Avoiding Indentation Errors:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician)#expected an indented block after 'for' statement on line 13

 magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")#The second print() call is not indented, so it is
#                                                                    executed only once after the loop has finished running. Because the final
#                                                                    value associated with magician is 'carolina', she is the only one who receives
#                                                                    the “looking forward to the next trick” message:


#unexpected indent
message = "Hello Python world!"
print(message)#unexpected indent if i gave a space at the start of this line..

#Forgetting the Colon  (:)
hi_list=["ji","hi"]
for hi in hi_list:
    print(hi,"\n")



#Exercise:
#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then 

pizza_list=["bbq sauce Pizza","chicken Tikka pizza","Special Pizza"]
#use a for loop to print the name of each pizza.
for pizza in pizza_list:
   print(pizza)
# Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni pizza.
   print(f"I like {pizza}..\n")
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as  I really love pizza!
print("I really like differenet pizza's types and their flavours they are good on tongue and also heavy on budget.......")


# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would make a great pet!

Animals=["Dog","Cat","Cow"]
for animal in Animals:
   print(animal)
   print(f"{animal}, can be made a great pet.")

print("Any of these above animals can be made a great pet...")


#Making Numerical Lists
for value in range(1,6):#we use range to to generate numbers based on our range with for loop.
   print(value)

numbers=list(range(1,6))#We can use list() to convert that same set of numbers into a list:
print(numbers)

#We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(),
#  Python uses that value as a step size when generating numbers.
for number in range(1,5):
   print(number)

#so if we are printing even numbers we would do it like this:
print("These are the even numbers i was talking about")
for value in range(0,11,2):#i started it from zeror and in 3rd  paramete i gave 2 to it wil jump 2 integers forward like from 0 to 2 then 4 and the 6. until it reach the range limit.
   print(value)


#create cubes of each number from 1 to 10:

cubes=[]

for value in range(1,11):
   cube=value**3
   cubes.append(cube)
print(cubes)

#for squares directly without using the square variable directly using append in init using value **2.
squares=[]

for value in range(1,11):
   squares.append(value**2)
print(squares)

# Focus first on writing code that you understand clearly, which does what you want it to do.Then look for more efficient approaches as you review your code.


# Simple Statistics with a List of Numbers
#finding max,min and sum of a list
numbers=[1,2,3,4,5]
print(max(numbers))
print(min(numbers))
print(sum(numbers))


#List Comprehensions (it is used when logic is simple and we want to write it in one line like combination of both loop and for loop).
squares=[value**2 for value in range(1,11)]
print(squares)

cube=[value**3 for value in range(1,11)]
print(cube)

#EXERCISE: 
#Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for value in range (1,21):
   print(value)

# One Million: Make a list of the numbers from one to one million, and thenuse a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)   

million_number=[value for value in range(1,1000001)]
print(million_number)

#Summing a Million: Make a list of the numbers from one to one million,and then use min() and max() to make sure your list actually starts at one andends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
print(min(million_number))
print(max(million_number))
print(sum(million_number))

# Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers=[value for value in range(1,21,2)]
print(odd_numbers)

# Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
threes=[value for value in range(3,31,3)]
print(threes)

# cube comprehension.Use a list comprehension to generate a list of the first 10 cubes.
cube=[value**3 for value in range(1,11)]
print(cube)
