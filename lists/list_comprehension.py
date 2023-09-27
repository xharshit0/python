def find_duplicates(lst):
    count_dict = {}
    duplicates = []
    
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    for item, count in count_dict.items():
        if count > 1:
            duplicates.append(item)
    
    return duplicates

my_list = [1, 2, 2, 3, 4, 4, 5]
duplicates = find_duplicates(my_list)
print(duplicates)
