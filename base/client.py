# from dbClient.query import *
from helpers import uri
from sqlalchemy import create_engine

class Database():
    """
    Base Client to interface database
    """
    def __init__(self,
                 auth:object):
        self.auth = auth
        
    def engine(self,database:str, **kwargs):
        return create_engine(self.auth.uri(database),pool = 900)