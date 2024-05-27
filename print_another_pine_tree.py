# Ask the user to enter their desired tree height
# Convert the value to integer
# Decrement spaces by 1 each time you loop through the range
# Increment the hashes by 2 each time you loop through the range
# Save spaces to the stump by calculating tree height - 1
# Print out the tree
tree_height = input("How tall is the tree? ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
tree_stump = tree_height - 1

while tree_height != 0:
    
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_stump -= 1
for i in range(tree_stump):
     print(' ', end="")
print("#")