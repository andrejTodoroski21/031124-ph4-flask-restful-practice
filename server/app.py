#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import WaterThing, UnderSeaHousing

from models import db # ADD OTHER MODELS HERE

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)


# ROUTES


@app.get('/')
def index():
    return { "stuff": "I am stuff" }, 404

@app.get('/water-things')
def get_all_water_things():
    return [water.to_dict() for water in WaterThing.query.all()], 200

@app.get('/water-things/<int:id>')
def get_by_id(id):
    water_thing = WaterThing.query.where(WaterThing.id == id).first()

    if water_thing:
        return water_thing.to_dict(), 200
    else: 
        return {"error":"Not fount"}, 404

@app.delete('/water-things/<int:id>')
def delete_water_things(id:int):
    water_thing_to_delete = WaterThing.query.where(WaterThing.id == id).first()
    
    if water_thing_to_delete:
        db.session.delete(water_thing_to_delete)
        db.session.commit()
        return{}, 204
    else:
        return {"error": "Not found"}, 404


@app.patch('/water-things/<int:id>')
def patch_water_things(id):
    water_thing_to_update = WaterThing.query.where(WaterThing.id == id).first()
    
    if water_thing_to_update:
        # name = request.json['name']
        for key in request.json.keys(): #name/species
            setattr(water_thing_to_update, key, request.json[key]) #set all keys for each key in request.json

        db.session.add(water_thing_to_update)
        db.session.commit()

        return water_thing_to_update.to_dict(), 202
    else:
        return {'error': 'Not found'}, 404




@app.post('/water-things')
def post_water_things():
    new_water_thing = WaterThing(
        name=request.json['name'], 
        species=request.json['species'])

    db.session.add(new_water_thing)
    db.session.commit()
     
    return new_water_thing.to_dict(), 201


# -----------------------under water housing table----------------------------------------------

@app.get('/housing')
def get_all_houses():
    return [house.to_dict() for house in UnderSeaHousing.query.all()], 200

@app.get('/housing/<int:id>')
def get_house_by_id(id):
    houses = UnderSeaHousing.query.where(UnderSeaHousing.id == id).first()

    if houses:
        return houses.to_dict(), 200
    else: 
        return {"error":"Not fount"}, 404

@app.delete('/housing/<int:id>')
def delete_houses(id:int):
    houses_to_delete = UnderSeaHousing.query.where(UnderSeaHousing.id == id).first()
    
    if houses_to_delete:
        db.session.delete(houses_to_delete)
        db.session.commit()
        return{}, 204
    else:
        return {"error": "Not found"}, 404


@app.patch('/housing/<int:id>')
def patch_houses(id):
    houses_to_update = UnderSeaHousing.query.where(UnderSeaHousing.id == id).first()
    
    if houses_to_update:
        # name = request.json['name']
        for key in request.json.keys(): #name/species
            setattr(houses_to_update, key, request.json[key]) #set all keys for each key in request.json

        db.session.add(houses_to_update)
        db.session.commit()

        return houses_to_update.to_dict(), 202
    else:
        return {'error': 'Not found'}, 404

@app.post('/housing')
def post_houses():
    new_house = UnderSeaHousing( 
        address=request.json['address'],
        residence = request.json['residence']
        )

    db.session.add(new_house)
    db.session.commit()
     
    return new_house.to_dict(), 201
# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)
