import die_roller as sm
import random


def choose_party(d_message):
    if "stepnov" in d_message.lower() and "roll party" in d_message.lower():
        party_array = ["Lucan","Lugosi","Grover"]
        roll_num = random.randint(0,2)
        return "Stepnov has chosen " + party_array[roll_num]
    else:
        print("Stepnov has nothing to say")

def die_rolls(d_message, user_n):
    if sm.die_roll_check(d_message):
        roll_params = sm.get_die_params(d_message)

        if isinstance(roll_params[0], int) and isinstance(roll_params[1], int):
            results, total = sm.roll_die(roll_params)
            return f"__## {user_n}'s {roll_params[0]}d{roll_params[1]} Roll##__\n**Results: **{results}\n**Total: ** {total}"

        else:
            print("Invalid input for rolling the die.")
    else:
        print(
            "Invalid input format. Please provide input in the format 'NdM', where N is the number of rolls and M is the type of die.")