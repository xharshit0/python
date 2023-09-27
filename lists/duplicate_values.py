def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

my_list = [1, 2, 2, 3, 4, 4, 5]
duplicates = find_duplicates(my_list)
print(duplicates)
