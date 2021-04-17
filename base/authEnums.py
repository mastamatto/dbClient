from enum import Enum

class DatabaseType(Enum):
    POSTGRES = 'postgresql'
    MYSQL    = 'mysql'
    
class ConnectorType(Enum):
    # POSTGRES
    PSYCOPG2 = 'psycopg2'
    PG8000   = 'pg8000'
    
    # MYSQL
    MYSQLDB  = 'mysqldb'
    PYMYSQL  = 'pymysql'