import ollama

base_attitude = "You are Stepnov. The spymaster for a dungeons and dragons campaign. You are a man of many appetites, mostly food related, and are known as the Hamlord. You speak like Nero Wolfe. You are the entity in control of the die rolls in my discord channel. Respond to the following as such and in less than 50 words. "

def stepnov_check(mess):
    if mess.startswith("STEPNOV"):
        return True
    else:
        False

def stepnov_speaks(mess):
    llama_model = 'llama3.2'
    the_query = base_attitude+mess

    stepnovs_response = ollama.chat(model=llama_model, messages =[
        {
            'role':'user',
            'content': the_query,
        },
    ])
    return  stepnovs_response['message']['content']

def stepnov_nat_1():
    the_query = base_attitude + "The player has rolled a nat 1. Mock them in 20 words or less."
    

