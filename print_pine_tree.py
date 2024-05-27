# Ask how long is the tree
# Convert the value to integer
# Decrement spaces by 1 each time you loop through the range
# Increment the hashes by 2 each time you loop through the range
# Save spaces to the stump by calculating tree height - 1

tree_height = input("How tall is the tree? ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
tree_stump = tree_height - 1
while tree_height != 0:
    print(" " * spaces + "#" * hashes)
    spaces -= 1
    hashes += 2
    tree_height -= 1