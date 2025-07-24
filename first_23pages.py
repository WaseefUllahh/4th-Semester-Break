print("hello World")
message="hello World this is in message variable."
print(message)

message2="This is python  crash course in the second program."
print(message2)
message_1="This is message no 1"
print(message_1)

message_3='this message uses two types of programs that uses "Python".'
print(message_3)

#operation of using method of title() upper and lower with variable and also formatting.
name_1="waseef ullah"
print(name_1.title())
print(name_1.lower())
print(name_1.upper())


first_name="Hamad"
Last_name="ahmad"

fuLL_name=f"{"First name is"} {first_name} {"and the last name is"} {Last_name} so the full name will be {first_name} {Last_name}"
greet_name=f"Hello, {first_name.title()} {Last_name.title()}!"

print(fuLL_name.upper())
print(greet_name)
format_name="{} {}".format(first_name, Last_name)
print(format_name.title())

#tabs and new line in print
print("Languages:\n\tjava\n\tPythonn\n\tC language\n\tWeb technology")


#now i will learn how to remove whit spaces from variable of diff types as it can be good during
# comparison with certain value like comparing user name on a website
# when he enters it and we compare it with already stored user name in our database.
favourite_language=" python is python  "
print(favourite_language)
print(favourite_language.lstrip())

my_age=1_000
print(my_age)
my_age2,my_age3=14,15
print(my_age2,my_age3)
