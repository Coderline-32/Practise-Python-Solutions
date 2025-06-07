a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Remove duplicates by converting to sets
set_a = set(a)
set_b = set(b)

# Find common elements using set intersection
common_elements = []

for item in set_a:
    if item in set_b:
        common_elements.append(item)

print(common_elements)
