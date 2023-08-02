import db_sqlite as db


def get_all() -> list:
    database = db.Database()
    data = database.data_select("medias")
    objects = []
    for t in data:
        objects.append(Media(t[0], t[1], t[2], t[3], t[4]))

    return objects


class Media():
    def __init__(self, id=None, name=None, type=None, path=None, description=None):
        self.id = id
        self.name = name
        self.type = type
        self.path = path
        self.description = description

        self.__table_name = "medias"


    def get_as_dict(self):
        representation = {}
        representation.update({"id": self.id})
        representation.update({"name": self.name})
        representation.update({"type": self.type})
        representation.update({"path": self.path})
        representation.update({"description": self.description})
        return representation


    def load(self, id):
        database = db.Database()
        data = database.data_select(self.__table_name, whereClause=f"id={id}")
        self.id = data[0]
        self.name = data[1]
        self.type = data[2]
        self.path = data[3]
        self.description = data[4]


    def save(self):
        database = db.Database()
        self.id = database.data_insert(self.__table_name, id=None, name=self.name, type=self.type, path=self.path, description=self.description)