from typing import Optional
from sqlalchemy import table
from sqlmodel import Field, Session, SQLModel, col, create_engine, or_, select

class Team(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    headsquarters:str


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    secret_name:str
    age: Optional[int]= Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

sqlite_file_name="database.db"
sqlite_url=f"sqlite:///{sqlite_file_name}"

engine= create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_heros():
    hero_1=Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2=Hero(name="Spider-Boy", secret_name="Pedro Pacativa")
    hero_3=Hero(name="Rosca-man", secret_name="Tommy Ésta", age=48)
    hero_4=Hero(name="Tarantula", secret_name="Natalia Romanov", age=35)
    hero_5=Hero(name="Black lion", secret_name="Trevor Wilis", age=40)
    hero_6=Hero(name="Doctor Strange", secret_name="Pachito", age=41)
    hero_7=Hero(name="Mefisto", secret_name="Arnolfo", age=90)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)

        session.commit()

def select_heros():

    with Session(engine) as session:
        statement = select(Hero).where(Hero.age < 40)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)

def update_heros():

    with Session(engine) as session:
        statement = select(Hero).where(Hero.name=="Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        print("Hero:", hero)

        hero.age=16
        session.add(hero)

        session.commit()
        session.refresh(hero)
        print("updated hero:", hero)



def main():
    create_db_and_tables()
    create_heros()
    select_heros()
    update_heros()

if __name__ == "__main__":
    main()