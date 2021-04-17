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
                 connector_type:str='pymysql',
                 db_type:str='mysql'):
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
    
    @property
    def header(self):
        return {'user':self.user,
                'password':self.password,
                'db_type':self.db_type,
                'connector_type':self.connector_type,
                'host':self.host,
                'port':self.port}

    def uri(self,database):
        hdr = self.header
        msg  = f"{hdr['db_type']}+{hdr['connector_type']}://"
        msg += f"{hdr['user']}:{hdr['password']}@"
        msg += f"{hdr['host']}:{hdr['port']}/{database}"
        return msg