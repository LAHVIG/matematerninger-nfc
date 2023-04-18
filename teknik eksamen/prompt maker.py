import random

dice_number = {1,2,3,4,5,6}
dice_operators = {"+","-","*","/"}

game_mode = "all"

prompt = []

def generate_prompt():
    if game_mode == "any":
        print ("any operator allowed")
        prompt[0] = random.choice(dice_number)
        prompt[1] = "?"
        prompt[2] = random.choice(dice_number)

    elif game_mode == "plus_minus":
        print("only plus and minus")
        temp_list = {dice_operators[0], dice_operators[1]}
        prompt[0] = random.choice(dice_number)
        prompt[1] = random.choice(temp_list)
        prompt[2] = random.choice(dice_number)

    elif game_mode == "div_mul":
        print("only division and multiplication")
        temp_list = {dice_operators[2], dice_operators[3]}
        prompt[0] = random.choice(dice_number)
        prompt[1] = random.choice(dice_operators)
        prompt[2] = random.choice(dice_number)
    elif game_mode == "random":
        print("choosing operator at random")
        prompt[0] = random.choice(dice_number)
        prompt[1] = random.choice(dice_operators)
        prompt[2] = random.choice(dice_number)

def calculate_prompt(prompt):
    if prompt[1] == "+":
        result = prompt[0] + prompt[2]
        return result
    elif prompt[1] == "-":
        result = prompt[0] - prompt[2]
        return result
    elif prompt[1] == "*":
        result = prompt[0] * prompt[2]
        return result
    elif prompt[1] == "/":
        result = prompt[0] / prompt[2]
        return result