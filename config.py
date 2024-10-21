import configparser
import os
import sys
CFG_FL='user.cfg'
USER_CFG_SECTION="sub_account"

class Config:
    def __init__(self):
        print("welcome to config module")
        config=configparser.ConfigParser()
        if os.path.exists("user.cfg"):
            config.read(CFG_FL)
            if USER_CFG_SECTION in config:
                print("Successfully fetch data")
            else:
                print("Section module is wrong or null")
                sys.exit(1)
                 
        
        else:
            print("No config file detected, exit")
            sys.exit(1)
        self.PC_API_KEY=config.get(USER_CFG_SECTION,"PC_API_KEY")
        self.PC_SECRET_KEY=config.get(USER_CFG_SECTION,"PC_SECRET_KEY")

        

