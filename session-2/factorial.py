"""
input: 5
output: 120
----
5! = 5 * 4!
4! = 4 * 3!
... 
1! = 1 

5! = 5 * 4 * 3 * 2 * 1 

"""
# get number
number = int(input("Enter a number: "))
result = 1
for i in range(number, 0, -1):
    result = result * i

print(f"result is {result}")
