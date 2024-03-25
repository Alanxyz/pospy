import sqlalchemy as sql
from .models import Base
from .models import Item

from .database import session as db
from .database import engine

def create_item(name, code):
    new_item = Item(name=name, code=code)
    db.add(new_item)
    db.commit()

def get_all_items():
    query = sql.select(Item)
    data = []
    for item in db.scalars(query):
        data.append({
            'id': item.id,
            'name': item.name,
            'code': item.code,
            'stock': item.stock
        })
    return data

def get_item_by_code(code):
    query = sql.select(Item).where(Item.code == code)
    item = db.scalars(query).one()
    return {
        'item': item.id,
        'name': item.name,
        'code': item.code,
        'stock': item.stock
    }

def get_item_by_id(id):
    query = sql.select(Item).where(Item.id == id)
    item = db.scalars(query).one()
    return {
        'item': item.id,
        'name': item.name,
        'code': item.code,
        'stock': item.stock
    }

def delete_item_by_id(id):
    query = sql.select(Item).where(Item.id == id)
    item = db.scalars(query).one()
    db.delete(item)
    db.commit()
