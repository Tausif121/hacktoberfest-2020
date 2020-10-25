# Program to convert temperature in celsius to fahrenheit 
# Input is provided by the user in degree celsius
 
# Take input from the user
celsius = float(input('Enter the temperature in degree Celsius: '))
 
# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
