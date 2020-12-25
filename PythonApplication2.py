
name = input("Please enter your First Name: ")
surname = input("Please enter your Last Name: ")
age = input("Please enter your Age: ")
birthday = input("Please enter your year of birth: ")
mylist = [name, surname, age, birthday]

for i in range(len(mylist)):
    print("{}".format(mylist[i]))

if int(age) < 18 :
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")