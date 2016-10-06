def insert_val_at(index, my_list, value):
    if index > len(my_list)-1:
        return False
    
    my_list.append('')
    
    for here in range(len(my_list)-1, index, -1):
        my_list[here] = my_list[here-1]

    my_list[index] = value

    return my_list

