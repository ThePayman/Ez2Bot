import Entity
def command(ctx,command,arg = None):
    if(Entity.player_exists(ctx.message.author.id)):
        player = [player for player in Entity.players if player.player_id == ctx.message.author.id][0]
        command_dictionary = {"travel":player.travel}
        arg_list = divide_args(arg)
        if(command in player.available_actions):
            command_dictionary[command](arg_list)

def divide_args(arg):
    arg_list = []
    current_word = ""
    for char in arg:
        if(char!=" "):
            current_word += char
        else:
            arg_list.append(current_word)
            current_word = ""
    if(current_word!=""):
        arg_list.append(current_word)
    return(arg_list)