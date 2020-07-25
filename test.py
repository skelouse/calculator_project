import math
import os

# Defines cls() to clear the screen of prints
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def add():
    cls()
    print('Adding')
    done = False
    while not done:
        try:
            n1 = float(input('Enter first number : '))
            print(n1, '+')
            n2 = float(input('Enter second number : '))
        except ValueError:
            print("Not a number!")
        done = True
        print(n1, '+', n2)
        print(' =', (n1+n2))

def subtract():
    cls()
    print('Subtracting')
    done = False
    while not done:
        try:
            n1 = float(input('Enter first number : '))
            print(n1, '-')
            n2 = float(input('Enter second number : '))
        except ValueError:
            print("Not a number!")
        done = True
        print(n1, '-', n2)
        print(' =', (n1-n2))

def multiply():
    cls()
    print('Multiplying')
    done = False
    while not done:
        try:
            n1 = float(input('Enter first number : '))
            print(n1, '*')
            n2 = float(input('Enter second number : '))
        except ValueError:
            print("Not a number!")
        done = True
        print(n1, '*', n2)
        print(' =', (n1*n2))

dquery = """
1. for normal division
2. for modulus division
3. for floor division
4. for swap numerator and denominator division
5. for all of the above

"""

def divide():
    cls()
    print('Dividing')
    done = False
    while not done:
        try:
            n1 = float(input('Enter first number : '))
            print(n1, '/')
            n2 = float(input('Enter second number : '))
        except ValueError:
            print("Not a number!")
        if n2 == 0.0:
            print("Cannot divide by zero")
        else:
            while not done:
                try:
                    print(n1, '/', n2)
                    select = input(dquery)
                    if select == '1':
                        print(n1, '/', n2)
                        print(' =', (n1/n2))
                        done = True
                    elif select == '2':
                        print(n1, '%', n2)
                        print(' =', (n1%n2))
                        done = True
                    elif select == '3':
                        print(n1, '//', n2)
                        print(' =', (n1//n2))
                        done = True
                    elif select == '4':
                        print(n2, '/', n1)
                        print(' =', (n2/n1))
                        done = True
                    elif select == '5':
                        print(n1, '/', n2, '=', (n1/n2))
                        print(n1, '%', n2, '=', (n1%n2))
                        print(n1, '//', n2, '=', (n1//n2))
                        print(n2, '/', n1, '=', (n2/n1))
                        done = True

                except ZeroDivisionError:
                    print("Can't divide by zero!")

def square_root():
    cls()
    done = False
    print('Square Rooting')
    while not done:
        try:
            n1 = float(input('Enter number : '))
            print('Square root of', n1, 'is', math.sqrt(n1))
            done = True
        except ValueError:
            print('Not a number!')
                
query = """
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square Root

q. Quit

Select an operation from the above : 
"""
select = None

while select != 'q':
    cls()
    select = input(query)

    if select == '1':
        add()
    elif select == '2':
        subtract()
    elif select == '3':
        multiply()
    elif select == '4':
        divide()
    elif select == '5':
        square_root()
    elif select == 'q':
        break
    input('press any key to continue')