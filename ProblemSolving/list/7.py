def remove_duplicate(items):
    new_item = []
    for item in items:
        if item in new_item:
            pass
        else:
            new_item.append(item)
    print(new_item)


remove_duplicate([10,20,30,20,10,50,60,40,80,50,40])
