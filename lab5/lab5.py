# 1. Generate two tuples to represent two distinct points in space (3D) and determine the Euclidean distance
p1 = tuple(int(x) for x in input("Enter coordinates of point 1: ").split())
p2 = tuple(int(x) for x in input("Enter coordinates of point 2: ").split())
distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2) ** 0.5
print(distance)

# 2. Find the equation of the straight line passing through these points (2D)
x1, y1 = p1[:2]
x2, y2 = p2[:2]
if x1 != x2 and y1 != y2:
    slope = (y2 - y1) / (x2 - x1)
    print(f"(x - {x1}) = {slope}(y - {y1})")
else:
    print("Vertical or horizontal line")

# 3. WAP to count the number of each character present in a string using the concept of a dictionary
s = input("Enter a string: ")
char_count = {ch: s.count(ch) for ch in s}
print(char_count)

# 4. Enter three lists using list comprehension: Customer name, Customer ID, and shopping points
customer_names = [name for name in input("Enter customer names: ").split()]
customer_ids = [int(id) for id in input("Enter customer IDs: ").split()]
shopping_points = [int(points) for points in input("Enter shopping points: ").split()]

# 5. Construct a list of tuples with and without using built-in function zip()
# Using zip()
customer_details_zip = list(zip(customer_names, customer_ids, shopping_points))
print(customer_details_zip)

# Without zip()
customer_details_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
print(customer_details_manual)

# 6. Sort the list of tuples constructed above with and without using the sorted function
# Using sorted()
sorted_customers_zip = sorted(customer_details_zip, key=lambda x: x[2])  # Sort by shopping points
print(sorted_customers_zip)

# Without sorted()
for i in range(len(customer_details_manual)):
    for j in range(i + 1, len(customer_details_manual)):
        if customer_details_manual[i][2] > customer_details_manual[j][2]:
            customer_details_manual[i], customer_details_manual[j] = customer_details_manual[j], customer_details_manual[i]
print(customer_details_manual)
