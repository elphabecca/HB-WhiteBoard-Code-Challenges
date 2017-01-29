
def shift_array(num_list, offset):

    offset = offset % len(num_list)

    if offset == 0:
        return num_list

    curr_value = num_list[0]
    for j in range(offset):
        print j, num_list           
        for i in range(len(num_list)):
            replace_index = i - 1
            replace_value = num_list[replace_index]
            num_list[replace_index] = curr_value
            curr_value = replace_value

    return num_list
            

    # replace_index = (curr_index - 2) % len(num_list)
    # replace_value = num_list[replace_index]
    # num_list[replace_index] = curr_value
    # curr_value = replace_value
    # curr_index = replace index