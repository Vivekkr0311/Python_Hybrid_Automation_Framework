# This file is used to read data from "ini" file.
# This file "readProperties" will use a python library called "configparser" to read
# data from the "ini" file.

import configparser

config = configparser.RawConfigParser()
config.read("/Users/vivek/PycharmProjects/Python_Hybrid_Automation_Framework/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        # This below line look for a 'common info' section in "ini" file
        # and from that section it looks for a key 'baseURL'.
        # If the value is present corresponding to the key, then
        # you will get the value here in 'url' variable.

        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password