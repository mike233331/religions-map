from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, Session


class Base(DeclarativeBase): pass


class Church(Base):
    __tablename__ = "church"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    coordinates = Column(String)
    description = Column(String)
    year_of_construction = Column(Integer)
    country_id = Column(Integer, ForeignKey("country.id"))
    religion_id = Column(Integer, ForeignKey("religion.id"))

    # country = relationship("Country", back_populates="churchs")
    # religion = relationship("religion", back_populates="churchs")


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    churchs = relationship("church", back_populates="church")


class Religion(Base):
    __tablename__ = "religion"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    churchs = relationship("church", back_populates="church")


engine = create_engine("sqlite:///../data/religion_01.db", echo = True)
Base.metadata.create_all(bind=engine)


with Session(autoflush=False, bind=engine) as db:
    #Создаем все религии
    Christianity = Religion(name="Christianity")
    Islam = Religion(name="Islam")
    Hinduism = Religion(name="Hinduism")
    Buddhism = Religion(name="Buddhism")
    Chinese_traditional_religion = Religion(name="Chinese traditional religion")
    African_traditional_religions = Religion(name="African traditional religions")
    print("with Session: ", db)
    db.commit()
print("db: ", db)

# with Session(autoflush=False, bind=engine) as db:
#     Georgia = Country(name="Georgia")
#     Egypt = Country(name="Egypt")
#     Belarus = Country(name="Belarus")
#     bolgaria = Country(name="bolgaria")
#     Serbia = Country(name="Serbia")
#     Greece = Country(name="Greece")
#     Romania = Country(name="Romania")
#     Ukraine = Country(name="Ukraine")
#     Ethiopia = Country(name="ethiopia")
#     Russia = Country(name="Russia")
#     db.commit()