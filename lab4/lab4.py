# 1. Find the number of palindrome words in the given sentence without defining any new function
sentence = input()
words = sentence.split()
print(sum(1 for word in words if word == word[::-1]))

# 2. Create a list of int using list comprehension [multiple input from keyboard]. Find the mean, median, and mode.
nums = [int(x) for x in input().split()]
mean = sum(nums) / len(nums)
sorted_nums = sorted(nums)

median = sorted_nums[len(nums) // 2] if len(nums) % 2 != 0 else (sorted_nums[len(nums) // 2] + sorted_nums[len(nums) // 2 - 1]) / 2
mode = max(set(nums), key=nums.count)
print(mean, median, mode)

# 3. Generate 2 lists (course code and course name) and create a new list with both.
course_code = input().split()
course_name = input().split()

course_details = [f"{code}:{name}" for code, name in zip(course_code, course_name)]
print(course_details)

# 4. Generate two sets – first for all singers and second for all dancers of the class using set comprehension.
singers = {x for x in input().split()}
dancers = {x for x in input().split()}
# DOIN the math here
all_artists = singers | dancers
allrounders = singers & dancers
dancers_not_singers = dancers - singers
singers_not_dancers = singers - dancers
exclusive_performers = dancers ^ singers

print(all_artists)
print(allrounders)
print(dancers_not_singers)
print(singers_not_dancers)
print(exclusive_performers)
