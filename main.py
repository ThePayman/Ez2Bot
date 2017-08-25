import discord
from discord.ext import commands
import logging
import asyncio
import DataBase
import Entity
import World

    
bot = commands.Bot(command_prefix="r/")
list = []

@bot.command(pass_context = True)
async def IsGay(ctx, *, member : discord.Member = None):
    if(member):
        if(member.id== "239669293975994369"):
            await bot.say("Kill is gaaay")
        elif(member.id == "253523108521181184"):
            await bot.say("Clutch? Gay? Nha... Even worst! He is a SAND NIGGER")
        elif(member.id == "247472262440026113"):
            await bot.say("Obviously.. He is my daddy ;)")
        else:
            if(int(member.id) % 2 == 1):
                await bot.say("Everyone is a little gay")
            else:
                await bot.say("Not gay")
    else:
        pass

@bot.command(pass_context = True)
async def actions(ctx):
    if(Entity.player_exists(ctx.message.author.id)):
        player = [player for player in Entity.players if player.player_id == ctx.message.author.id][0]
        for i in range(len(player.available_commands)):
            await bot.say(str(i+1) + " - " +player.available_commands[i])

@bot.command(pass_context = True)
async def do(ctx, *, args = None):
    #args is a string, needs to be separated into multiple args
    try:
        action = args[0]
        arg = args[2]
    except:
        action = args[0]
        arg = None
    if(Entity.player_exists(ctx.message.author.id)):
        player = [player for player in Entity.players if player.player_id == ctx.message.author.id][0]
        try:
            action = int(action)
            if(action in range(len(player.available_commands)+1)):
                action  = player.available_commands[action-1]
        except:
            pass
        if(action in player.available_commands):
            await bot.say(player.action(action,arg))
                
@bot.command(pass_context = True)
async def search(ctx):
    if(Entity.player_exists(ctx.message.author.id)):
        enemyE = Entity.Zombie(ctx.message.author.id)
        Entity.enemies.append(enemyE)
        enemy_list_player = [enemy for enemy in Entity.enemies if enemy.attached_player == ctx.message.author.id]
        await bot.say("You found "+str(len(enemy_list_player))+" Monsters:")
        for enemy in enemy_list_player:
            if (enemy.attached_player == ctx.message.author.id):
                await bot.say("> "+enemy.type+" HP: "+str(enemy.hp)+" Dmg: "+str(enemy.strength))

    
bot.run("MzQ5MTQ1NjA1ODgyMzgwMjg4.DH0Ilw.f3__DcHYTe0rPEAtRoOybN1sNIg")
