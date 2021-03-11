"""
a 
b
oprator


a + b 
a * b 
a / b 
a // b 
a  % b 

"""
def add(a , b):
    return a + b
def product(a, b):
    return a * b 
def sub(a, b):
    return a - b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def div_int(a, b):
    return a // b 




lst_of_oprators = ['+', '*', '/', '//' , '%']
dict_of_oprators = {
    '+': add,
    '*':product,
    '/':div,
    '//':div_int,
    '%':mod,
}
while True:
    number_a = int(input('Enter Number a: '))
    number_b = int(input('Enter Number b: '))
    oprator = input('Enter Operator: ')
    if oprator in dict_of_oprators:
        print("oprator is correct")

        result = dict_of_oprators[oprator](number_a, number_b)
        print(result)
        print(number_a, number_b, oprator)
        print(
        f"a: {number_a} , b: {number_b} \n  {number_a} {oprator} {number_b} = {result}")

    else:
        print("oprator is not correct")

