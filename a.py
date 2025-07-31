# 1. Custom length
def custom_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# 2. Custom sum
def custom_sum(lst):
    total = 0
    for item in lst:
        total += item
    return total

# 3. Custom max
def custom_max(lst):
    if custom_length(lst) == 0:
        return None
    max_val = lst[0]
    for item in lst[1:]:
        if item > max_val:
            max_val = item
    return max_val

# 4. Custom min
def custom_min(lst):
    if custom_length(lst) == 0:
        return None
    min_val = lst[0]
    for item in lst[1:]:
        if item < min_val:
            min_val = item
    return min_val

# 5. Custom reverse
def custom_reverse(lst):
    reversed_list = []
    i = custom_length(lst) - 1
    while i >= 0:
        reversed_list += [lst[i]]  # manually adding
        i -= 1
    return reversed_list

# 6. Custom count
def custom_count(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

# 7. Custom index (first occurrence)
def custom_index(lst, value):
    i = 0
    for item in lst:
        if item == value:
            return i
        i += 1
    return -1  # Not found

# 8. Custom copy
def custom_copy(lst):
    copied = []
    for item in lst:
        copied += [item]
    return copied

# 9. Custom merge
def custom_merge(lst1, lst2):
    merged = []
    for item in lst1:
        merged += [item]
    for item in lst2:
        merged += [item]
    return merged

# 10. Custom sort (bubble sort)
def custom_sort(lst):
    n = custom_length(lst)
    sorted_list = custom_copy(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
    return sorted_list

# --------------------
# Test the functions
# --------------------

data = [5, 3, 8, 3, 1]

print("Original:", data)
print("Length:", custom_length(data))
print("Sum:", custom_sum(data))
print("Max:", custom_max(data))
print("Min:", custom_min(data))
print("Reversed:", custom_reverse(data))
print("Count of 3:", custom_count(data, 3))
print("Index of 8:", custom_index(data, 8))
print("Copied list:", custom_copy(data))
print("Merged list:", custom_merge(data, [7, 9]))
print("Sorted list:", custom_sort(data))
