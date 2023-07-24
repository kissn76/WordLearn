import db_sqlite as db


def main():
    database = db.Database()
    # database.create_tables()
    database.types_get()


if __name__ == '__main__':
    main()