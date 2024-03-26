# Q1: write a program a print first 10 natural number
for i in range(1,11):
    print(i)
# Q2: write a program to print first 10 even numbers
for i in range(1,11):
    if i%2 == 0:
        print(i)
# Q3: write a program to print first 10 odd numbers
for i in range(1,11,2):
    print(i)
# Q4: write a program to print first 10 even numbers in reverse order
for i in range(10,0,-2):
    print(i)
# Q5: 1
#     2 2
#     3 3 3
#     4 4 4 4
for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()
# Q6: 4 4 4 4
#     3 3 3
#     2 2
#     1
for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
    print()
# Q7: 
a = [1,2,3]
b = ["what","why","when"]
for i in a:
    for j in b:
        print(i,j)
# Q8:
a = [7,9]
b = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    for j in b:
        print(f"{i}x{j}={i*j}")
    print()
