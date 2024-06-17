# types
print(type(1).__name__)
print(type(-1).__name__)
print(type(0).__name__)
print(type(0.0).__name__)
print(type(2.2).__name__)
print(type(4E2).__name__)
# Arithmetics
print(10/3) # 3.3333
print(10//3) #  3 ---> return floor - no decimal and return integer
print(10 % 3) # 1 ---> modulo operator - only returns reminder good for finding old and even no 

#Basic functions

pow(5,2) #  25 doing 5 ** 2 
abs(-50) # 50 
round(5.468, 2) # 5.46 --> round to nth digit
bin(512) # '0b1000000' -> binary format
hex(512) # '0x200' -> hexadecimanl

# Converting Strings to Numbers
# age = input("How old are you ?")
# age = int(age)
# pi = input("What is the value of pi?")
# pi = float(pi)

# Strings 
type("Helloooo")  #str


'I \'m thirsty'
"I'm thirsty"
"\n" # new line
"\t" # adds a tab
print('Hey you!'[4]) #y


name = 'Andrei Neagoie'

name[4] # e
name[:] # Andrei Neigoie
name[1:] #ndrei Neagoie
name[:1] # A
name[-1] # e
name[::1] # Andrei Neogoie -> displaying last to first 
name[::-1] # eioogoeN ierdnA -> reverse display
name[0:10:2]  # Ade e

# : is called slicing and has the format [start: end : step]

'Hi there' + 'Timmy' # this is called string concatinations 

"*"*10 # ***********

# Basic Functions

len('turtle') # 6

# Basic Methods 
'  I am alone  '.strip() # 'I am alone' --> Strips all whitespace

#characters from both ends.

'On an island'.strip('d') # 'On an islan' --> # Strips all passed , it only replaces 

'On an island'.replace('a','') # 'On n islnd' --> # Strips all passed , it only replaces 

str = 'On an island'
new_str = ''
for char in str:
    if char != 'a':
        new_str +=char
print(new_str)

# characters from both ends.

print('but life is good!'.split())

print('help me'.replace('me','you'))
#  second param

print('Need to make fire'.startswith('Need')) # True

print('and cook rice'.endswith('rices')) # True

print('bye bye'.index('e')) # 2

print('still there?'.upper()) # STILL THERE?

print('HELLO?!'.lower()) # hello?!
print('ok, I am done'.capitalize())

print('oh hi there'.find('i')) # 4 --> return the starting 
#  index position of the first occurrence
'oh hi there'.count('e') # 2

#  String Formatting

# name1 = "Andrei"
# name2 = 'Sunny'

# print(f'Hello there {name1} and {name2}')

# print('Hello there {} and {}'.format(name1, name2))

# print('Hello there %s and %s' %(name1,name2))

# # Sunny --> you can also use %d, %f, %r for integers, floats, string 
# # representations of objects respectively

# word = "reviver"

# p = bool(word.find(word[::-1] + 1))

'''
   let's break it down 
    1. word[::-1] reverses the word
    2. word.find when found the work it will return index in this case 0 , if not -1
    3. +1 because , it needs to be presented with boolean so 1 or 0  will be accounted as True or False
'''

text = "This is a string with a substring"
substring = 'substring'

start = text.find(substring)
end = start + len(substring)
if start != -1:
    print(f"The substring  {substring} is found at starting {start} and end {end}")
else:
    print("The substring is not found in the text")




