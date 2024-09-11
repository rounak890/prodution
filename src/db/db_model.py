from sqlalchemy import REAL, INTEGER, VARCHAR
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from config.config import settings

class Base(DeclarativeBase):
    pass

class RentApartments(Base):
    __tablename__ = settings.rent_apart_table_name # since we might have some other name & similar structure
    address : Mapped[str] =  mapped_column(VARCHAR(), primary_key = True) # since primary key is neccesary
    area : Mapped[float] =  mapped_column( REAL())
    constraction_year : Mapped[int] =  mapped_column(INTEGER())
    rooms : Mapped[int] =  mapped_column(INTEGER())
    bedrooms : Mapped[int] =  mapped_column(INTEGER() )     
    bathrooms : Mapped[int] =  mapped_column(INTEGER())     
    balcony: Mapped[str] =  mapped_column( VARCHAR())
    storage : Mapped[str] =  mapped_column(VARCHAR())
    parking : Mapped[str] =  mapped_column(VARCHAR())
    furnished : Mapped[str] =  mapped_column(VARCHAR())
    garage : Mapped[str] =  mapped_column(VARCHAR())
    garden : Mapped[str] =  mapped_column(VARCHAR())
    energy : Mapped[str] =  mapped_column(VARCHAR())
    facilities : Mapped[str] =  mapped_column(VARCHAR())
    zip : Mapped[str] =  mapped_column(VARCHAR())
    neighborhood : Mapped[str] =  mapped_column(VARCHAR())
    rent : Mapped[int] =  mapped_column(INTEGER())
    