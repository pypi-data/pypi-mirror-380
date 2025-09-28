from pynetbox.core.response import Record

class Configurations(Record):
    pass

class Platforms(Record):
    pass

class Routers(Record):
    platform = Platforms