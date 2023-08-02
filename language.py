import db_sqlite as db


def get_all() -> list:
    database = db.Database()
    data = database.data_select("languages")
    objects = []
    for t in data:
        objects.append(Language(t[0], t[1], t[2]))

    return objects


class Language():
    def __init__(self, code=None, name=None, description=None):
        self.code = code
        self.name = name
        self.description = description

        self.__table_name = "languages"


    def get_as_dict(self):
        representation = {}
        representation.update({"code": self.code})
        representation.update({"name": self.name})
        representation.update({"description": self.description})
        return representation


    def load(self, code):
        database = db.Database()
        data = database.data_select(self.__table_name, whereClause=f"code={code}")
        self.code = data[0]
        self.name = data[1]
        self.description = data[2]


    def save(self):
        database = db.Database()
        database.data_insert(self.__table_name, code=self.code, name=self.name, description=self.description)
