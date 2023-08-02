import db_sqlite as db


def get_all() -> list:
    database = db.Database()
    data = database.data_select("phonetics")
    objects = []
    for t in data:
        objects.append(Phonetic(t[0], t[1], t[2], t[3]))

    return objects


class Phonetic():
    def __init__(self, id=None, word_id=None, language_code=None, phonetic=None):
        self.id = id
        self.word_id = word_id
        self.language_code = language_code
        self.phonetic = phonetic

        self.__table_name = "phonetics"


    def get_as_dict(self):
        representation = {}
        representation.update({"id": self.id})
        representation.update({"word_id": self.word_id})
        representation.update({"language_code": self.language_code})
        representation.update({"phonetic": self.phonetic})
        return representation


    def load(self, id):
        database = db.Database()
        data = database.data_select(self.__table_name, whereClause=f"id={id}")
        self.id = data[0]
        self.word_id = data[1]
        self.language_code = data[2]
        self.phonetic = data[3]


    def save(self):
        database = db.Database()
        self.id = database.data_insert(self.__table_name, id=None, word_id=self.word_id, language_code=self.language_code, phonetic=self.phonetic)