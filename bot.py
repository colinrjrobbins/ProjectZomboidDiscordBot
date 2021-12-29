# Name: bot.py
# Desc: Project Zomboid Discord Bot
# Date: 2021-12-29
# Purp: Used to check the IP of the server and send it to
#       the Discord chat if it has changed, also to restart
#       the server if it has stopped. 

import discord
import os
from modules.IPGather import IPGather
from modules.ServerCheck import ServerCheck

client = discord.Client()

ipg = IPGather()
sc = ServerCheck()

# watchdog for the running server
    # if server has stopped restart it
    # check and save the IP address gathered
# check to see if IP changed 
    # if IP has changed update the file
    # send new IP to discord chat. 

client.run(os.getenv('TOKEN'))