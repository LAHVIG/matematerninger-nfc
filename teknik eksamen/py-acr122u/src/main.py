data_list = [[0,0],[0,0],[0,0]]
"""list of position and values from dice"""
import nfc
from threading import Thread
import time
from graphics import *
from prompt_maker import *

has_been_solved = True
"""bool to check if the prompt has been solved by the user"""
#set to true to start game
graphics = Graphics()

calibrated_order = []

dice_table = [[[25, 12, 182, 110],1],
              [[89, 22, 180, 109],2],
              [[57, 175, 190, 110],3],
              [[70, 230, 97, 249],4],
              [[23, 43, 95, 179],5],
              [[133, 22, 249, 194],6],
              [[4, 74, 54, 170, 12, 89, 129],"master"],
              [[4, 70, 74, 194, 110, 103, 129],"/"],
              [[4, 81, 202, 18, 20, 111, 128],"-"],
              [[4, 66, 74, 194, 110, 103, 129],"*"],
              [[4, 62, 74, 194, 110, 103, 129],"+"],
              [[4, 129, 223, 1, 24, 64, 3],1],
              [[4, 92, 74, 194, 110, 103, 129],2],
              [[4, 139, 248, 170, 162, 64, 128],3],
              [[4, 78, 201, 18, 20, 111, 128],4],
              [[4, 30, 112, 194, 110, 103, 128],5],
              [[4, 85, 202, 18, 20, 111, 128],6]]

print("the whole list ",dice_table)
print("the first side ",dice_table[0])
print("the first id ",dice_table[0][0])
print("the first number ",dice_table[0][1])

def placement_correct(data_in):
    """takes in data_list and checks if the dice are placed correctly"""
    if data_in[0][0] in ["/","-","*","+"] or data_in[2][0] in ["/","-","*","+"] or data_in[1][0] in [1,2,3,4,5,6]:
        return False
    elif data_in[0][0] in [1,2,3,4,5,6] or data_in[2][0] in [1,2,3,4,5,6] or data_in[1][1] in ["/","-","*","+"]:
        return True

def replace_value_by_index(my_list, index, new_value):
    """
    Replace the value at the given index in my_list with new_value.
    """
    if index < len(my_list):
        my_list[index] = new_value
    return my_list


def compare_id(list_in, id_in):
    #print(id_in)
    for i in list_in:
        if i[0] == id_in:
            return i[1]

def parse_data(data_in, position_in):
    dice_id = data_in
    position = remap_position(position_in, calibrated_order)
    dice_number = compare_id(dice_table, dice_id)
    return [dice_number, position]


def remap_position(original_position, position_map):
    if len(position_map) != 3:
        #print("original position: " ,original_position)
        return original_position
    else:
        mapped_position = position_map.index(original_position) + 1
        #print("original position: " ,original_position)
        return mapped_position

checked_indexes = [0,1,2]

def calibrate(list_in):
    """takes in data list and calibrates the order of the readers"""
    if len(calibrated_order) == 3:

        return calibrated_order
    calibrated = False
    if not calibrated:
        for i in checked_indexes:
            if list_in[i][0] == 'master':
                calibrated_order.append(list_in[i][1])
                checked_indexes.remove(i)
        #print(calibrated_order)


while(1):
    time.sleep(0.1)

    if has_been_solved:
        prompt = generate_prompt("plus_minus")
        prompt_answer = calculate_prompt(prompt)
        has_been_solved = False

    try:
        reader0 = nfc.Reader(0)
        readerData0 = reader0.get_data(reader0.get_uid())
        data_placeholder = parse_data(readerData0,1)
        data_list = replace_value_by_index(data_list, 0, data_placeholder)
        print("parsed data: ",data_list[0])


    except:
        ""
    try:
        reader1 = nfc.Reader(1)
        readerData1 = reader1.get_data(reader1.get_uid())
        data_placeholder = parse_data(readerData1,2)
        data_list = replace_value_by_index(data_list, 1, data_placeholder)
        print("parsed data: ",data_list[1])

    except:
        ""
    try:
        reader2 = nfc.Reader(2)
        readerData2 = reader2.get_data(reader2.get_uid())
        data_placeholder = parse_data(readerData2,3)
        data_list = replace_value_by_index(data_list, 2, data_placeholder)
        print("parsed data: ",data_list[2])
        
        
    except:
        ""
    calibrate(data_list)

    chopped_data = str(data_list[0][0]) + str(data_list[1][0]) + str(data_list[2][0])

    if placement_correct(data_list):
        graphics.update_text(chopped_data+"="+str(prompt_answer))
        graphics.update_symbol("solved")
    else:
        graphics.update_text("place the dice correctly!")
        graphics.update_symbol("wrong")

    graphics.window.update_idletasks()
    graphics.window.update()


