def replace_value_by_index(my_list, index, new_value):
    """
    Replace the value at the given index in my_list with new_value.
    """
    if index < len(my_list):
        my_list[index] = new_value
    return my_list


def compare_id(list_in, id_in):
    print(id_in)
    for i in list_in:
        if i[0] == id_in:
            return i[1]

def parse_data(data_in, position_in,dice_table):
    dice_id = data_in
    position = position_in
    dice_number = compare_id(dice_table, dice_id)
    return [dice_number, position]

checked_indexes = [0,1,2]
def calibrate(list_in, calibrated_order):
    ""
    
    for i in checked_indexes:
        if list_in[i][0] == 'master':
            calibrated_order.append(list_in[i][1])
            checked_indexes.remove(i)
    if len(calibrated_order) == 3:
        ""