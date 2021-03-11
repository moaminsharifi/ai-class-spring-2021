"""
input: 50943

5: 55555
0:
9: 999999999
4: 4444
3: 333

"""
number = input("Enter a number: ")
for char in number:
    print(f"{char}: {char * int(char)}")
