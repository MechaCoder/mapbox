from tinydb_base import User
from os.path import isfile

class Users(User):

    def __init__(self, table: str = __name__, requiredKeys='username,password'):
        file = 'ds.json'
        if isfile('.dev'):
            print('Developer Mode Actvated :: ', table)
            file = 'ds.dev.json'
        super().__init__(file=file, table=table, requiredKeys=requiredKeys)
