First_name = input("Enter your first name")
Last_name = input("Enter last name")
Login = First_name + " "+ Last_name
print(Login)

# How to do a running list with python

data = []

while True:
    name = input("Enter items : ")
    data.append(name)

    choice = input("Enter another Item?? (y/n) : ")

    if choice.casefold() == 'n':
        break

    for element in data:
        print(element)