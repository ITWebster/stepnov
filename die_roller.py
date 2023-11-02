import random

def die_roll_check(mess):
    if mess and mess[0].isdigit():
        return True
    else:
        return False


def get_die_params(mess):
    parsed_string = mess.split("d")
    total_rolls = int(parsed_string[0])
    die_type = int(parsed_string[1])
    return total_rolls, die_type


def roll_die(roll_params):
    results = []
    total = 0
    total_rolls, die_type = roll_params
    for _ in range(total_rolls):
        die_roll = random.randint(1, die_type)
        results.append(die_roll)
        total += die_roll
    return results, total