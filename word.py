import db_sqlite as db


def get_all() -> list:
    database = db.Database()
    data = database.data_select("words")
    objects = []
    for t in data:
        objects.append(Word(t[0], t[1], t[2], t[3]))

    return objects


class Word():
    def __init__(self, id=None, word=None, type_code=None, connection_id=None):
        self.id = id
        self.word = word
        self.type_code = type_code
        self.connection_id = connection_id

        self.__table_name = "words"


    def get_as_dict(self):
        representation = {}
        representation.update({"id": self.id})
        representation.update({"word": self.word})
        representation.update({"type_code": self.type_code})
        representation.update({"connection_id": self.connection_id})
        return representation


    def load(self, id):
        database = db.Database()
        data = database.data_select(self.__table_name, whereClause=f"id={id}")
        self.id = data[0]
        self.word = data[1]
        self.type_code = data[2]
        self.connection_id = data[3]


    def save(self):
        database = db.Database()
        self.id = database.data_insert(self.__table_name, id=None, word=self.word, type_code=self.type_code, connection_id=self.connection_id)
