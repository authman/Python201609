def insert_val_at(index, my_list, value):
    # delete the pass below and write the implementation here
    if not index in range(len(my_list)):
        return False
    out = my_list[0:index]
    out.append(value)
    out += my_list[index:]
    my_list = out
    return my_list

# **** tried to make a faster version by not using slice*****
# def insert_val_at(index, my_list, value):
#     # delete the pass below and write the implementation here
#     out = []
#     if not index in range(len(my_list)):
#         return False
#     for i in range(index):
#         out.append(my_list[i])
#     out.append(value)
#     for i in range(index,len(my_list)):
#         out.append(my_list[i])
#     my_list = out
#     return my_list
