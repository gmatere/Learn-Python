types_of_people = 10 #assigning value to a variable
x = f"There are {types_of_people} types of people." #defining vairable x with a formatted string

binary = "binary" #assigning value to a variable
do_not = "don't" #assigning value to a variable

y = f"Those who understand {binary} and those who {do_not}." #defining vairable y with a formatted string

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = "True"
joke_evaluation = "Isn't that joke is funny? {}"

print(joke_evaluation.format(hilarious)) #passing the value of vairable hilarious to another variable which is joke_evaluation


e = "This is the left side of the msg..."
w = "and this is right side!!"

print(e+w) # adding 2 strings