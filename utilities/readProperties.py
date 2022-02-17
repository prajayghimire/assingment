import configparser

con = configparser.RawConfigParser()
con.read(".\\config\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():

        url= con.get('COMMON INFO', 'baseURL')
        return url



