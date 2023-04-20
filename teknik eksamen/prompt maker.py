import random

dice_number = ["1","2","3","4","5","6"]
dice_operators = ["+","-","*","/"]


def generate_prompt(game_mode):
    """takes in the game mode that decides the prompt"""
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
    
def calculate_user(answer):
    """takes in the users answer and calculates the value"""

prompt = generate_prompt("plus_minus")

result = calculate_prompt(prompt)
print(prompt)
print(result)