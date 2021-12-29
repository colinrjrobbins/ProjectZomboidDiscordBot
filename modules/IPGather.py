import os, fnmatch
import getpass

class IPGather:
    def __init__(self):
        self.username = getpass.getuser()
        self.file_pattern = '*DebugLog-server.txt'
        self.search_pattern = 'Public IP:'

    def file_find(self, path):
        result = []
        for root, dirs, files in os.walk(os.getcwd()):
            for name in files:
                if fnmatch.fnmatch(name, self.file_pattern):
                    result.append(os.path.join(root, name))
        return result[0]
    
    def log_search(self, logString):
        index = logString.find(self.search_pattern)
        gatheredIP = logString[index+11:index+26]
        ipList = gatheredIP.split('.')
        ip = "{}.{}.{}.{}".format(
            ipList[0],
            ipList[1],
            ipList[2],
            ipList[3]
        )
        return ip

    # primary run check
    def run_ip_check(self):
        os.chdir('/home/{}/Zomboid/Logs/'.format(self.username))
        cwd = os.getcwd()
        log_file = self.file_find(cwd)
        save_log = open(log_file, 'r')
        lines = str(save_log.read())
        public_IP = log_search(lines)
        return public_IP