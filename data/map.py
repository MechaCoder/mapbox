from .base import Base

class Map(Base):

    def __init__(self, table: str = __name__, requiredKeys='uuid:str,title:str,bgimg:str,scimg:str,scon:bool'):
        super().__init__(table=table, requiredKeys=requiredKeys)

    def create(self, title:str, background:str, screensaver:str):

        row = {
            'uuid': self._create_uuid(),
            'title': title,
            'bgimg': background,
            'scimg': screensaver,
            'scon' : True
        }

        return super().create(row=row)
