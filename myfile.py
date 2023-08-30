print("Hello future Python programmer!");\
print("Python is a great language");\
print(2. ** 3.)
print(2 ** 3)
print(13 / 4 + 13 % 4)
print(10 - 6 ** 2 / 9 * 10 + 1)
print(2*(2+3))
print(10 / 2)
print(6. // 4)
x = 10 / 4
y = 5 / 2.0
print (x + y)
print(2 * 3 ** 3 * 4)
print(2 ** 3.)

#variables
amount_of_apples = 2
cost_of_apple = 5
print(amount_of_apples * cost_of_apple);\

# cost 2 increased by 2 = 4 multiply by 4 = 16
amount = 4
cost = 2
cost += 2
print(amount * cost);\

# 22 divide by 2 = 12; 12 + 44 = 55.0
age = 22
AGE = 44
age /= 2
print(age + AGE);\

# strings has higher prio than int
y = 5
y = "Jack"
print(y);\

#NAME ERROR (TypeError: unsupported operand type(s) for +: 'float' and 'str')

#x = 5
#y = 6
#z = 7
#print(x+y+z)

#print("Hello, jack!")
print("Hello, Sally!");\


#print Sally#123
name = "Sally"# employee name
 
data = "#123" 
print (name+data);\

#input
favorite_color = ("What is your favorite color?")
print("Your favorite color is " + favorite_color);\

#input

age =input("My age is: " )
print (age);\

# It prompts for the string and then output would be: "Hello Python&"" would be the output

inputString = input('Enter a string: ')
print(inputString, sep='#', end='&\n');\

#STRING METHOD

Num = input("Enter a Number: ") 
print (Num * 3 );\

#Which method should you use in order to convert the input into a string correctly. 
# The answer is str function and + plus sign to concatenate


year_of_birth = int(input("In what year were you born? "))

print("You were born in " + str(year_of_birth));\

#What is the output of the following python code if we enter 5 as input? Ans. 15
Num = input("Enter a Number: ")
Num = int(Num) 
print ( Num * 3 );\

#What is the output of the following python code? Ans. 5Sally

x = 5
y = "Sally"
print(str(x) + y);\

#What is the output of the following python code if we enter “HelloPython” as input?
#Ans. HelloPythonHelloPython

inputString = input('Enter a string: ')
print(inputString*2);\

#What will be printed when the following executes? Ans. haha

print("ha"*2);\

#What is the output of the following python code if we enter 5 as input?
#Ans. 555 
#variable Num = input is a string 
#therefore the output would be treated as a string unless concatenated with an int

Num = input("Enter a Number: ") 
print (Num * 3 );\

#COMPARISON OPerators

#What would get printed?

min_score = 13
score = 13

print(score > min_score) # False
print(score <= min_score) # True 

#What is the output when the following executes? Ans. False

print(2 < 4);\

#What is the output of the following python code?
#Ans: True

x = 6
y = 7
print(x != y);\

#Conditional Statements;

#What is the output of the following python code?
#ANS. b is greater than a

a = 5
b = 10
if b < a:
  print("a is greater than b")
elif a == b:
  b = 5
  print("a and b are equal")
else:
  print("b is greater than a");\
  
#What is the output of the following python code?
#ANS. The negative number -10 is not valid here. This is always printed....
# the lack of "else" syntax prints the second statement also.

x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed");\

#What is the output of the following python code?
#ANS. (assuming that there is no indentation) "indentation error " since there is no indentation for the variable print
# otherwise the result would be "b is greater than a"

a = 5
b = 10
if b > a:
    print("b is greater than a");\
    
#What does the following Python program display?
#ANS. "Or here Or over here?"
# the lack of "else" syntax prints the second statement also.
x = 3
if ( x == 0 ):
  print("Am I here?")
elif ( x == 3 ):
  print("Or here?")
  print("Or over here?");\
  



#Which one of the following if statements will not execute successfully ?
#ANS. 2nd statemenet.
#2nd statement: IndentationError: expected an indented block, 3rd statement: NameError: name 'yes' is not defined. 
#NOTE: The condition in if statement is (5,10), which is a tuple containing the values 5 and 10. 
#In Python, non-empty containers like tuples are considered "truthy,"
#meaning they are treated as true in a boolean context.


# 1st if statement
#if True: print('hello')

# 2nd if statement
#if (5,10):
  #print('hello') # assuming that there is no indentation to this stamenent

# 3rd if statement
#if (yes):
  #print('hello')

# 4th if statement
#if (5,10): print('hello');\





#Given the nested if-else below, what will be the value x when the code executed successfully.
# ANS: 4
# if statuement is false;
# elif statement is false;
# else statment is true; so the answer is 4
# the last else statement won't run as the first else statements satisfies the true answer.

x = 0
a = 6
b = 6
if a > 0:
    if b < 0: 
        x = x + 6 
    elif a > 6:
        x = x + 5
    else:
        x = x + 4
else:
    x = x + 3

print(x);\


#Which statement will check if a is equal to b?
# if a = b; if a ===c; if (a ==b )
#In Python, you can also use parentheses around the condition in an if statement, and it will not affect the functionality. The parentheses can be used for readability or to clarify the order of operations in more complex conditions. 
#So both the statements "if (a == b):" and "if a == b:" are correct.


#LOOPS
secret_number = 3
guess = int(input("Guess a number: "))
while guess != secret_number:
   guess = int(input("Guess a number: "))
else:
   print("Congratulations, you guess the secret number!");\

#What will be the output of the following Python code?
#5
#6
#7
#8

i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1;\
    
#What will be the output of the following Python code?
#1
#2

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1;\
    
#What will be the output of the following Python code?
#ANs 123456

i = 1
while True:
    if i % 0o7 == 0:
        break
    print(i)
    i += 1    
    
#What does the following code produce as output?
#ANS: 6

i = 1
x = 3
sum = 0
while ( i <= x ):
 sum += i
 i += 1
print(sum);\

#What is the output when this code executes?

x = 1
while ( x <= 5 ):
  x += 1
print(x);\


#What is the value of x …

x = 51


while (x < 50):
  x+=2

print(x);\

#LISTS

#What will be the output of below Python code?
#ANS:[10,13]

list1 = [10, 11, 12, 13, 14]
print(list1[::3]);\

#What will be the output of below Python code?
#ANS: [10,2,3,4,5] array 1 replaced by 10;

list1 = [1, 2, 3, 4, 5]
list1[0] = 10
print(list1);\

#What will be the output of below Python code?
#ANS: 6

numbers = [1, 2, 3, 4, 5]
numbers[4] = 6
print(numbers[4]);\

#What will be the output of below Python code?
ANS: [4,4,1]

list1 = [4, 4, 3, 1]
list1.pop(2)
print(list1);\

#What will be the output of following Python code?
#ANS: C

list1=["Go","Java","C","Rust"]
print(min(list1));\

#What will be the output of below Python code?
#Hint: with insert method, 
#we can insert a new item in between values so item 8 will be inserted into index 1; 1 being the index
#and "8" is the new value in the list.
#ANS: ['UK',8,'India','Canada']

list1=['UK','India','Canada']

list1.insert(1,8)

print(list1);

#What will be printed by the following code when it executes?
#ANS: 19 ( 0 + the sum total of the numbers within the array)

sum = 0
values = [2,9,1,7]
for number in values:
    sum = sum + number

print(sum);\

#Which of the following statements won’t be printed when this Python code is run?
#ANS: u

for letter in 'KodeKloud':
    if letter == 'u':
        continue
    print('Letter : ' + letter);\
    
#Which of the following statements won’t be printed when this Python code is run?
#ANS: e

for letter in 'KodeKloud':
    if letter == 'e':
        continue
    print('Letter : ' + letter);\
    
       







    































