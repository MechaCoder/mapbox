from os.path import isfile
from tinydb_base import DatabaseBase
from .exceptions import NotImplermented
from .utilities import makeUuid

class Base(DatabaseBase):

    def __init__(self, table: str = ..., requiredKeys='title:str'):
        file = 'ds.json'
        if isfile('.dev'):
            print('Developer Mode Actvated :: ', table)
            file = 'ds.dev.json'
        super().__init__(file=file, table=table, requiredKeys=requiredKeys)
        self.uuidLength = 8

    def _create_uuid(self):

        if 'uuid' not in self.requiredKeys:
            raise NotImplermented('uuid is not implmented on this table')

        while True:
            uuid = makeUuid(self.uuidLength)
            if self.exists('uuid', uuid):
                continue
            return uuid
