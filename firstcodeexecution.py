name = input("Enter your name: ")
age = int(input("enter your age: "))
print("Hello, " + name + "! Welcome to the program.")   
print("name: " + name)
print("age: " + str(age))
row = 5
for i in range (row +3):
    for j in range(i+9):
        print("*", end="")
    print()
