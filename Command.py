def command(ctx, arg = None):
    if(Entity.player_exists(ctx.message.author.id)):
        player = [player for player in Entity.players if player.player_id == ctx.message.author.id][0]
        return True

def divide_args(arg):
    args = []
    return args
