# Project Zomboid Discord Bot
Used for a Dedicated Project Zomboid Server

## Purpose
To keep the server running and keep the potential users of the server updated if the IP changes.

## Current Commands
### server-status
Checks to see if the server is running
    Returns: IP Address, Port and Server Status

## TODO
### restart
Forces a stop and restart of the server, can only be run if the server is currently in an up state.

### start-server
Starts the server. Can only be run if the server is in a down state.

## Files
### bot.py
Used to create the bot and run everything.

### .env
Contains a TOKEN for the Discord Bot

### localIP.txt
Used to store the IP address for the Server and keep track of when to update and message the Discord chat

## Classes
### ServerCheck
Checks to see if the server is running, if it is not running, then start or restart a new instance of it for minimum downtime.

### IPGather
Checks the initial Debug log files and determines the IP address that is currently being used by the server. As the debug file is updated the system will recheck the IP and only notify upon change.