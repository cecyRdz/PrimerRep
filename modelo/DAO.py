from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean, BLOB

db = SQLAlchemy()

class Productos(db.Model):
    __tablename__='productos'
    IDPRODUCTO=Column(Integer, primary_key=True)
    IDCATEGORIA=Column(Integer)
    NOMBRE=Column(String(50))
    DECRIPCION=Column(String(100))
    PRECIO=Column(Float)
    EXISTENCIA=Column(Integer)
    COLOR=Column(String(25))
    MARCA=Column(String(50))
    COSTOENVIO=Column(Float)
    ESTATUS= Column(Boolean,default=True)
    foto=Column(BLOB)

    def insertar (self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual (self,id):
        return self.query.get(id)

    def actualizar (self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,id):
        objeto= self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral (self):
        return self.query.all()