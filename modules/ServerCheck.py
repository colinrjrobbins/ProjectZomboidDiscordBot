import os

class ServerCheck:
    def __init__(self):
        pass
    
    def string_modify(self):
        catch = os.popen('ps aux | grep "SCREEN -S server bash start.sh"').read()
        catch_split = catch.split("\n")
        return catch_split[0]
    
    def restart_server(self):
        pass
        # restart the server

    # primary run check
    def server_running(self):
        split_string = self.string_modify()
        if "ps aux" in split_string:
            return False
        elif "grep" in split_string:
            return False
        else:
            return True