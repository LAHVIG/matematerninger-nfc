# import ndef
# from ndef.message import message_encoder, message_decoder
# import nfc

#reader0-2, left to right

#testing lol

data_list = [[0,0],[0,0],[0,0]]
from src import nfc
from threading import Thread
import time

calibrated_order = []

dice_table = [[[25, 12, 182, 110],1],[[89, 22, 180, 109],2],[[57, 175, 190, 110],3],[[70, 230, 97, 249],4],[[23, 43, 95, 179],5],[[133, 22, 249, 194],6],[[4, 79, 53, 170, 12, 89, 129],"master"],[[4, 70, 74, 194, 110, 103, 129],"division"],[[4, 81, 202, 18, 20, 111, 128],"subtraction"],[[4, 66, 74, 194, 110, 103, 129],"multiplication"],[[4, 62, 74, 194, 110, 103, 129],"addition"],[[4, 129, 223, 1, 24, 64, 3],1],[[4, 92, 74, 194, 110, 103, 129],2],[[4, 139, 248, 170, 162, 64, 128],3],[[4, 78, 201, 18, 20, 111, 128],4],[[4, 30, 112, 194, 110, 103, 128],5],[[4, 85, 202, 18, 20, 111, 128],6]]
print("the whole list ",dice_table)
print("the first side ",dice_table[0])
print("the first id ",dice_table[0][0])
print("the first number ",dice_table[0][1])

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

def parse_data(data_in, position_in):
    dice_id = data_in
    position = position_in
    dice_number = compare_id(dice_table, dice_id)
    return [dice_number, position]

checked_indexes = [0,1,2]
def calibrate(list_in):
    ""
    
    for i in checked_indexes:
        if list_in[i][0] == 'master':
            calibrated_order.append(list_in[i][1])
            checked_indexes.remove(i)
    if len(calibrated_order) == 3:
        ""

   # print(calibrated_list)

    #brug master kort
    #check for alle læsere
    #læs log
    #første entry bliver første i lsit calibrated_order
    #anden, anden
    #tredje,, tredje
    #når en aflæst og sat i liste, bliver der ikke lyttet mere på den
    #når alle er aflæst gås der til normal mode





while(1):
    time.sleep(0.1)

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
    print(calibrated_order)


