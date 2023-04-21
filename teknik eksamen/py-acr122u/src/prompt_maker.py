import random

dice_number = ["1","2","3","4","5","6"]
"""list of all possible number dice sides"""
dice_operators = ["+","-","*","/"]
"""list of all possible operator dice sides"""


def generate_prompt(game_mode):
    """any, random, div_mul, plus_minus. takes in the game mode that decides the prompt"""
    prompt = ["","",""]
    if game_mode == "any" or game_mode == "random":
        print ("any operator allowed")
        prompt[0] = random.choice(dice_number)
        prompt[1] = random.choice(dice_operators)
        prompt[2] = random.choice(dice_number)
        return prompt

    if game_mode == "plus_minus":
        print("only plus and minus")
        temp_list = [dice_operators[0], dice_operators[1]]

    elif game_mode == "div_mul":
        print("only division and multiplication")
        temp_list = [dice_operators[2], dice_operators[3]]

    prompt[0] = random.choice(dice_number)
    prompt[1] = random.choice(temp_list)
    prompt[2] = random.choice(dice_number)
    return prompt

def calculate_prompt(prompt):
    """takes in the prompt and calculates the value"""
    #is it cursed?
    #yes
    return eval(prompt[0]+prompt[1]+prompt[2])
    
def calculate_user(answer, result, game_mode):
    """takes in the users answer and calculates the value"""
    #check if operators are the same
    stripped_data = [str(answer[0][0]),str(answer[1][0]),str(answer[2][0])]
    return calculate_prompt(stripped_data) == result

def correct_op(usr_in, game_mode):
    stripped_data = [str(usr_in[0][0]),str(usr_in[1][0]),str(usr_in[2][0])]
    user_op = stripped_data[1]

    if game_mode == "mul_div":
        if not user_op in ["*","/"]:
            return False
    if game_mode == "plus_minus":
        if user_op in ["+", "-"]:
            return False
    return True 

prompt = generate_prompt("plus_minus")

result = calculate_prompt(prompt)
print(prompt)
print(result)