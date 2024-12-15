import random

def die_roll_check(mess):
    if mess and mess[0].isdigit():
        return True
    else:
        return False

def get_die_params(mess):
    parts = mess.split("d")
    total_rolls = int(parts[0])

    # Splitting the second part to handle modifiers
    if '+' in parts[1]:
        die_type, modifier = map(int, parts[1].split('+'))
        modifier = +modifier  # Positive modifier
    elif '-' in parts[1]:
        die_type, modifier = map(int, parts[1].split('-'))
        modifier = -modifier  # Negative modifier
    else:
        die_type = int(parts[1])
        modifier = 0  # No modifier

    return total_rolls, die_type, modifier

def roll_die(roll_params):
    results = []
    total = 0
    total_rolls, die_type, modifier = roll_params
    for _ in range(total_rolls):
        die_roll = random.randint(1, die_type)
        results.append(die_roll)
        total += die_roll
    total += modifier
    return results, total