mylist = [27,18,50,12,41,52,63,54,94,70]
highest,lowest=0,0
lowest = mylist[0]
for items in mylist:
    print(mylist)
    if items>highest:
        highest = items
    elif items<lowest:
        lowest=items
print("lowest is",lowest)
print("highest is",highest)
    
