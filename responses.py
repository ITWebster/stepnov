import die_roller as sm
import stepnov_ai as sai

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
        
def stepnov_ai(d_message, user_n):
    step_check = sai.stepnov_check(d_message)
    print(step_check)
    if sai.stepnov_check(d_message):

        stepnovs_wisdom = sai.stepnov_speaks(d_message)
        return stepnovs_wisdom
    else:
        print("Stepnov has nothing to say")
