# Ask the user to enter desirable tree height
# Convert the height to integer
# Decrement spaces by 1 each time you loop through the range
# Increment the stars by 2 each time you loop through the range
# Save spaces to the stump by calculating tree height - 1
tree_height = input("How tall do you want the tree to be? ")
tree_height = int(tree_height)
spaces = tree_height - 1
stars = 1
stump = tree_height - 1
while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(stars):
        print('*', end="")
    print()
    spaces -= 1
    stars += 2
    tree_height -= 1
for i in range(stump):
    print(' ', end="")
print("*")