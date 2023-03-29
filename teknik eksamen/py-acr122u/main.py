from src import nfc
from threading import Thread
import time
from nfcFnc import *

calibrated_order = []
data_list = [[0,0],[0,0],[0,0]]

dice_table = [[[25, 12, 182, 110],1],
              [[89, 22, 180, 109],2],
              [[57, 175, 190, 110],3],
              [[70, 230, 97, 249],4],
              [[23, 43, 95, 179],5],
              [[133, 22, 249, 194],6],
              [[4, 79, 53, 170, 12, 89, 129],"master"],
              [[4, 70, 74, 194, 110, 103, 129],"division"],
              [[4, 81, 202, 18, 20, 111, 128],"subtraction"],
              [[4, 66, 74, 194, 110, 103, 129],"multiplication"],
              [[4, 62, 74, 194, 110, 103, 129],"addition"],
              [[4, 129, 223, 1, 24, 64, 3],1],
              [[4, 92, 74, 194, 110, 103, 129],2],
              [[4, 139, 248, 170, 162, 64, 128],3],
              [[4, 78, 201, 18, 20, 111, 128],4],
              [[4, 30, 112, 194, 110, 103, 128],5],
              [[4, 85, 202, 18, 20, 111, 128],6]]


print("The whole list ",dice_table)
print("The first side ",dice_table[0])
print("The first id ",dice_table[0][0])
print("The first number ",dice_table[0][1])

while(True):
    time.sleep(0.1)
    
    allReaders = listOfReaders()
    for i, reader in enumerate(allReaders):
        readerData = reader.get_data(reader.get_uid())
        data_placeholder = parse_data(readerData,i+1,dice_table)
        data_list = replace_value_by_index(data_list, i, data_placeholder)
        print("Parsed data: ",data_list[i])


