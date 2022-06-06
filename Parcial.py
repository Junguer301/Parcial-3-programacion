from typing import Optional
from sqlalchemy import table
from sqlmodel import SQLModel, Field, Session, create_engine, select


class Medios(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    medio: str = Field(index=True)
    indice_de_refraccion: float = Field(default=None)


class velocidad_medio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    velocidad_Luz: Optional[float] = Field(default=None, index=True)

    refraccion_n_id: Optional[int] = Field(default=None, foreign_key= "medios.id")


base_de_datos="Base de datos V_luz.db"
url_base_de_datos=f"sqlite:///{base_de_datos}"

motor = create_engine(url_base_de_datos, echo=True)

def crear_db_y_tablas():
    SQLModel.metadata.create_all(motor)


def medios():

    medio_1=Medios(medio="vacío", indice_de_refraccion=1)
    medio_2=Medios(medio="aire", indice_de_refraccion=1.0002)
    medio_3=Medios(medio="agua", indice_de_refraccion=1.333)
    medio_4=Medios(medio="café", indice_de_refraccion=1.345)
    medio_5=Medios(medio="miel", indice_de_refraccion=1.520)
    medio_6=Medios(medio="cerveza", indice_de_refraccion=1.346)
    medio_7=Medios(medio="diamante", indice_de_refraccion=2.417)

    with Session(motor) as sesion:
            
        sesion.add(medio_1)
        sesion.add(medio_2)
        sesion.add(medio_3)
        sesion.add(medio_4)
        sesion.add(medio_5)
        sesion.add(medio_6)
        sesion.add(medio_7)

        sesion.commit()
        

def selec_medio():

    with Session(motor) as sesion:

      seleccion=select(Medios, velocidad_medio).where(Medios.id==velocidad_medio.refraccion_n_id)  
      resultados=sesion.exec(seleccion)
      medios_selec=resultados.all()
      print(medios_selec)



def velocidad():
    c=3*10**8
    velocidad_1=velocidad_medio(velocidad_Luz=c/1)
    velocidad_2=velocidad_medio(velocidad_Luz=c/1.0002)
    velocidad_3=velocidad_medio(velocidad_Luz=c/1.333)
    velocidad_4=velocidad_medio(velocidad_Luz=c/1.345)
    velocidad_5=velocidad_medio(velocidad_Luz=c/1.520)
    velocidad_6=velocidad_medio(velocidad_Luz=c/1.346)
    velocidad_7=velocidad_medio(velocidad_Luz=c/2.417)

    with Session(motor) as sesion:

        sesion.add(velocidad_1)
        sesion.add(velocidad_2)
        sesion.add(velocidad_3)
        sesion.add(velocidad_4)
        sesion.add(velocidad_5)
        sesion.add(velocidad_6)
        sesion.add(velocidad_7)
        
        sesion.commit()
        

def main():
    crear_db_y_tablas()
    medios()
    selec_medio()
    velocidad()
    
if __name__ == "__main__":
    main()


