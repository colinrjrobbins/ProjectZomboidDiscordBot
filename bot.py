# Name: bot.py
# Desc: Project Zomboid Discord Bot
# Date: 2021-12-29
# Purp: Used to check the IP of the server and send it to
#       the Discord chat if it has changed, also to restart
#       the server if it has stopped. 

from discord.ext import commands
import os
from modules.IPGather import IPGather
from modules.ServerCheck import ServerCheck

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='$')

ipg = IPGather()
sc = ServerCheck()

@bot.command(name='server-check', help='Responds with server status.')
async def server_check(ctx):
    server_check = sc.server_running()
    print(f'Server Running: {server_check}')
    server_ip = ipg.run_ip_check()
    with open('localIP.txt', 'w') as ip_file:
        ip_file.write(server_ip)
    print(f'IP Address: {server_ip}')
    print('Server Port: 16261')

    response = f'Server Running: {server_check}\nIP Address: {server_ip}\nServer Port: 16261'
    await ctx.send(response)

# check to see if IP changed 
    # if IP has changed update the file
    # send new IP to discord chat. 

bot.run(TOKEN)
