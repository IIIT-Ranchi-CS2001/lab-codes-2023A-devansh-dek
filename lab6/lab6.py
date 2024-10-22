################## 1
def my_zip(customer_name, customer_id, shopping_points):
        # Zip by taking the minimum length of the lists
        min_length = min(len(customer_name), len(customer_id), len(shopping_points))
        return list(zip(customer_name[:min_length], customer_id[:min_length], shopping_points[:min_length]))
customer_name = ['Alice', 'Bob', 'Charlie']
customer_id = [101, 102, 103]
shopping_points = [500, 300, 450]

res = my_zip(customer_name, customer_id, shopping_points)
print(res)


################# 2
def my_sort(data, key=0):
    n = len(data)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]

    return data
sortedOne= my_sort(res, key=0)

print(f"Sorted one is {sortedOne}")

#################3
def my_max(container):
    if len(container) == 0:
        return None  
        maxx_val = container[0]
    
    for val in container:
        if val > maxx_val:
            maxx_val = val
    
    return maxx_val
arr = [1,3,4,1]
maxx = my_max(arr)
print(maxx)