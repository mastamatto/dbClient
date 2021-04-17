import os

class Authorization:
    """
    dbClient/base/authorization
    """
    def __init__(self,
                 user:str,
                 password:str,
                 host:str,
                 port:int,
                 db_type:str='mysql',
                 connector_type:str='pymysql'):
        self.user            = user
        self.password        = password
        self.db_type         = db_type
        self.connector_type  = connector_type
        self.host            = host
        self.port            = int(port)
    
    @classmethod
    def fromEnv(cls):
        obj = cls(user     = os.environ.get('DB_UN'),
                  password = os.environ.get('DB_PW'),
                  host     = os.environ.get('DB_HOST'),
                  port     = os.environ.get('DB_PORT'))
        return obj
    
    @classmethod
    def fromDict(cls,configDict):
        obj = cls(user     = configDict.get('user'),
                  password = configDict.get('password'),
                  host     = configDict.get('host'),
                  port     = configDict.get('port'))
        return obj

    def uri(self,database):
        msg  = f"{self.db_type}+{self.connector_type}://"
        msg += f"{self.user}:{self.password}@"
        msg += f"{self.host}:{self.port}/{database}"
        return msg