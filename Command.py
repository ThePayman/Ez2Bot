import Entity
def command(ctx,command,arg = None):
    if(Entity.player_exists(ctx.message.author.id)):
        player = [player for player in Entity.players if player.player_id == ctx.message.author.id][0]
        command_dictionary = {"travel":player.travel}
        if(arg):
            arg_list = divide_args(arg)
        else:
            arg_list = None
        if(command in player.available_commands):
            return (command_dictionary[command](arg_list))

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
