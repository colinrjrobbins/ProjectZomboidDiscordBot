import os

class ServerCheck:
    def __init__(self):
        self.catch = os.popen('ps aux | grep "SCREEN -S server bash start.sh"').read()
        self.server_up = True

    def string_modify(self):
        catch_split = self.catch.split("\n")
        return catch_split[0]
    
    def restart_server(self):
        pass
        # restart the server

    # primary run check
    def server_running(self):
        split_string = string_modify()
        if "ps aux" in split_string:
            return False
        elif "grep" in split_string:
            return False
        else:
            return True