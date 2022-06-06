from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    secret_name:str
    age: Optional[int]=None

sqlite_file_name="database.db"
sqlite_url=f"sqlite:///{sqlite_file_name}"

engine= create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_heros():
    hero_1=Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2=Hero(name="Spider-Boy", secret_name="Pedro Pacativa")
    hero_3=Hero(name="Rosca-man", secret_name="Tommy Ésta", age=48)

    print("Antes de interactuar con la base de datos")
    print("hero_1", hero_1)
    print("hero_2", hero_2)
    print("hero_3", hero_3)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        print("Despues de agregarlo a la base de datos")
        print("hero_1", hero_1)
        print("hero_2", hero_2)
        print("hero_3", hero_3)

        session.commit()

        print("despues de committing la sesion")
        print("hero_1", hero_1)
        print("hero_2", hero_2)
        print("hero_3", hero_3)

        print("despues de committing la sesion, muestre IDs")
        print("hero_1 ID", hero_1.id)
        print("hero_2 ID", hero_2.id)
        print("hero_3 ID", hero_3.id)

        print("despues de committing la sesion, muestre names")
        print("hero_1 NAME", hero_1.name)
        print("hero_2 NAME", hero_2.name)
        print("hero_3 NAME", hero_3.name)

        session.refresh(hero_1)
        session.refresh(hero_2)
        session.refresh(hero_3)

        print("despues de refreshear los heros")
        print("hero_1", hero_1)
        print("hero_2", hero_2)
        print("hero_3", hero_3)
    
    print("despues de cerrar sesion")
    print("hero_1", hero_1)
    print("hero_2", hero_2)
    print("hero_3", hero_3)

   

def main():
    create_db_and_tables()
    create_heros()



if __name__ == "__main__":
    main()