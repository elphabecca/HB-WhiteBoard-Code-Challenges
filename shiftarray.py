
def shift_array1(num_list, offset):

    offset = offset % len(num_list)

    if offset == 0:
        return num_list

    curr_value = num_list[0]
    curr_index = 0
    for i in range(len(num_list)):
        replace_index = (curr_index - offset) % len(num_list)
        replace_value = num_list[replace_index]
        num_list[replace_index] = curr_value
        curr_value = replace_value
        curr_index = replace_index

    return num_list 


def shift_array2(num_list, offset):

    offset = offset % len(num_list)

    if offset == 0:
        return num_list

    for j in range(offset):
        curr_value = num_list[0]
        k = -1
        for i in range(len(num_list)):
            replace_index = k
            replace_value = num_list[replace_index]
            num_list[replace_index] = curr_value
            curr_value = replace_value
            k -= 1

    return num_list