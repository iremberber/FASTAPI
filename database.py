from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL bağlantı URL'si
DATABASE_URL = "postgresql://postgres:12345@localhost/GYK1Northwind"

# SQLAlchemy engine oluştur
engine = create_engine(DATABASE_URL)

# Oturum yönetimi için session oluştur
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base sınıfı tanımla (tüm modeller bundan türetilecek)
Base = declarative_base()