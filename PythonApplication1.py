mylist = list()

for i in range(5):
    value = input("Please enter a value: ")
    mylist.append(value)
    type(value)

for i in range(5):
    print("value: {} - type: {}".format(mylist[i],type(mylist[i])))