from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import crud, models
from database import SessionLocal, engine

# FastAPI uygulamasını başlat
app = FastAPI()

# Veritabanı bağlantısını yöneten fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic modelleri
class ProductCreate(BaseModel):
    product_name: str
    unit_price: float

class ProductUpdate(BaseModel):
    product_name: str = None
    unit_price: float = None

# Veritabanı tablolarını uygulama başlatıldığında manuel olarak oluştur
models.Base.metadata.create_all(bind=engine)

# Tüm ürünleri getir
@app.get("/products")
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

# Tüm siparişleri getir
@app.get("/orders")
def read_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

# Yeni ürün ekle
@app.post("/products")
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product.dict())

# Ürünü güncelle
@app.put("/products/{product_id}")
def update_existing_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product.dict(exclude_unset=True))
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

# Ürünü sil
@app.delete("/products/{product_id}")
def delete_existing_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"} 