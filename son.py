from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column

Base = declarative_base()


class Son(Base):
    __tablename__ = "son"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(50))

    @property
    def full_name(self):
        return "{0} {1}".format(self.name, self.last_name)

if __name__ == "__main__":
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
