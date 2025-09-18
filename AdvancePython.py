# List Creation
my_list = [1, 2, 3, 4]

# Access
print(my_list[0])      # First element
print(my_list[-1])     # Last element

# Update



my_list[1] = 20        # [1, 20, 3, 4]

# Add elements
my_list.append(5)      # [1, 20, 3, 4, 5]
my_list.insert(2, 99)  # [1, 20, 99, 3, 4, 5]
 

# Remove elements
my_list.remove(20)     # Remove by value → [1, 99, 3, 4, 5]
del my_list[0]         # Remove by index → [99, 3, 4, 5]
my_list.pop()          # Pops last element → [99, 3, 4]

# Length
print(len(my_list))    # 3

# Sort and Reverse
my_list.sort()         # [3, 4, 99]
my_list.reverse()      # [99, 4, 3]

# Slicing
print(my_list[1:3])    # [4, 3]

# Membership test
print(3 in my_list)    # True

# Copy
copy_list = my_list.copy()

# Clear
my_list.clear()        # []

# Final Output
print("Original list:", my_list)
print("Copied list:", copy_list)
