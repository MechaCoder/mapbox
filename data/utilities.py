from string import ascii_lowercase, digits
from random import choices


def makeUuid(l:int = 8):

    pool = choices(ascii_lowercase + digits, k=5000)
    uuid = choices(pool, k=l)
    return ''.join(uuid)