from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# MODELS
class WaterThing(db.Model):
    __tablename__ = 'water_things_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'speceis':self.species
        }

class UnderSeaHousing(db.Model):
    __tablename__ = 'under_water_housing_table'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    residence = db.Column(db.String)

    def to_dict(self):
        return {
            'id':self.id,
            'address':self.address,
            'residence':self.residence
        }


# WRITE MODELS HERE