#Question 1 Write a program to print 'F' to 'A' in five different lines.
# for i in range(5,-1,-1):
# # add 65 to current value and print ascii character output F E D C B A
#  i = i + 65
#  print(chr(i))

#Question 2 Write a program to read and store the name of three different cities in three different variables and print all the contents of variables on the console.
# city1 = str(input('Enter first city name:'))
# city2 = str(input('Enter Second city name:'))
# city3 = str(input('Enter first third city name:'))
#
# print('Entered city names are:')
# print(city1)
# print(city2)
# print(city3)

#3 Write a program to prompt the user to enter and display their personal details, such as name, address and mobile number.

# name = str(input('Enter your name: '))
# add = str(input('Enter your address: '))
# mob = str(input('Enter your mobile number: '))
#
# print("Enter details are:")
# print('Name: ',name)
# print('Address: ',add)
# print('Mobile number: ',mob)

#4 by making use of five different print statements, write a program to print 'A' to 'F' in one single line.

# print('A',end=' ')
# print('B',end=' ')
# print('C',end=' ')
# print('D',end=' ')
# print('E',end=' ')

#5 write a program to read an integer as a string. Convert the string into interger and display the type of value before and after converting to int

# var = str(input('Enter an integer. '))
# print(var)
# var = int(var)
# print('After converting the string into interger')
# print(var)

#6 Write a program initialize the string “hello world” to a variable Str1 and convert the string into upper case.
# str1 = 'hello world'
# print(str1)
# str2 = str1.upper()
# print('After converting into uppercase\n',str2)

#7 Translate the following algorithm into Python code.
'''Step 1: Initialize variable named Pounds with value 10.
 Step 2: Multiply Pounds by 0.45 and assign it to a variable Kilogram.
 Step 3: Display the value of variable Pounds and Variable.'''

# Pounds = 10
# Kilogram = 0.45*Pounds
#
# print('Pounds =',Pounds)
# print('Killogram =',Kilogram)


#8. Write a program to read the radius of a circle and print the area of the circle.
r = int(input("Enter radius of the circle: "))
pie = 3.14
area = pie*r*r
print('Area = ',area)