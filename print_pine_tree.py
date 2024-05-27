# How long is the tree? 10
# Use 1 while loop and 3 for loops to print a pine tree

tree_height = input("How long is the tree? ")

tree_height = int(tree_height)

for i in range(tree_height):
    for j in range(tree_height-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()