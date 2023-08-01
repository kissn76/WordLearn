import db_sqlite as db


def types_get():
    database = db.Database()
    data = database.data_select("types")
    types = {}
    for t in data:
        types.update({t[0]: WordType(t[0], t[1], t[2])})

    return types


class WordType():
    def __init__(self, code=None, name=None, description=None):
        self.code = code
        self.name = name
        self.description = description

        self.__table_name = "types"


    def load(self, code):
        database = db.Database()
        data = database.data_select(self.__table_name, whereClause=f"code={code}")
        self.code = data[0]
        self.name = data[1]
        self.description = data[2]


    def save(self):
        database = db.Database()
        database.data_insert(self.__table_name, code=self.code, name=self.name, description=self.description)