#exeption handling
#function

#get value using index.Atleast 2
#copy the list to another list called my_furniture
#using loops display each element

furniture = ['Bed', 'Table','Chair', 'Stool','Cupboard']
print(furniture[1])
print(furniture[2])

my_furniture = furniture
print("This is my_furniture list:", my_furniture)
for item in my_furniture:
    print(item)

    #getting theindex in a loop with enumerate()
    for index,item in enumerate(my_furniture):
        print(f'index:{index} - item:{item}')
        # print('index: {}'.format(index) -'item'.format(item))
        #display the cost of each item usung the zip()
        #create a list of 5 integer value andcall it price

price = [100, 900, 789,765, 500]
print(price)
for item, amount in zip(my_furniture, price):
    print(f'The {item} costs ksh {amount}')

    #Exception handling
num = int(input('Enter the value'))
print(num)

# try and except function, works more or less as a function block
try:
    num = int(input('Enter the value'))
    print(num)
except ValueError:
    print("Enter a number")
except ZeroDivisionError:
    print('Do not by zero')
    


