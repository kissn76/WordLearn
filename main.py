import db_sqlite as db


def main():
    database = db.Database()
    database.create_tables()


if __name__ == '__main__':
    main()