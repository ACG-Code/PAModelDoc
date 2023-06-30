from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from base_settings import application_path

Base = declarative_base()


class PyDB(Base):
    __tablename__ = 'secrets'

    id = Column('id', Integer, primary_key=True)
    secret = Column('secret', String, unique=True, nullable=False)
    username = Column('username', String, nullable=False)
    password = Column('password', String, nullable=False)


class DB(PyDB):
    def __init__(self):
        super().__init__()
        db = application_path + '/secrets.db'
        self.engine = create_engine('sqlite:///' + db)
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_secrets(self, secret: str, username: str, password: str):
        db = PyDB()
        db.secret = secret
        db.username = username
        db.password = password
        self.session.add(db)
        self.session.commit()

    def retrieve_secrets(self, secret: str):
        stmt = f"select * from secrets where secret = '{secret}'"
        conn = self.engine.connect()
        with conn:
            _results = conn.execute(stmt)
            results = list(_results)
            if len(results) > 0:
                _user = results[0][2]
                _pass = results[0][3]
                return _user, _pass
            else:
                print(f"Secret {secret} does not exist in database")
                raise exit(-1)

    def update_secret(self, secret: str, username: str or None, password: str):
        if username:
            stmt = f'UPDATE secrets set username="{username}", password="{password}" where secret="{secret}"'
        else:
            stmt = f'UPDATE secrets set password="{password}" where secret="{secret}"'
        conn = self.engine.connect()
        with conn:
            _results = conn.execute(stmt)

    def delete_secret(self, secret: str):
        stmt = f"DELETE FROM secrets where secret='{secret}'"
        conn = self.engine.connect()
        with conn:
            _results = conn.execute(stmt)

    def secret_exists(self, secret: str) -> bool:
        stmt = f"SELECT username from secrets where secret='{secret}'"
        conn = self.engine.connect()
        with conn:
            _results = conn.execute(stmt)
            _results = list(_results)
            if len(_results) > 0:
                return True
            else:
                return False
