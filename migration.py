from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:filipe1020@localhost:5432/RickandMorty'
db = SQLAlchemy(app)


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    status = db.Column(db.String(200))
    species = db.Column(db.String(200))
    type = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.String(200))
    origin_name = db.Column(db.String(200))
    location_name = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def __init__(self, name, status, species, type, gender, origin_name, location_name, image):
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin_name = origin_name
        self.location_name = location_name
        self.image = image


@app.route('/home/', methods=['GET', 'POST'])
def welcome():
    with open('C:\\Users\\Filipe Costa Levar\\Desktop\\Eitree Academy\\jsontoimport.json', encoding='utf-8-sig') as file:
        characters_data = json.load(file)

    sorted_characters = sorted(characters_data, key=lambda x: x["id"])

    for character in sorted_characters:
        name = character['name']
        status = character['status']
        species = character['species']
        type = character['type']
        gender = character['gender']
        origin_name = character['origin']['name']
        location_name = character['location']['name']
        image = character['image']

        char = Character(name, status, species, type, gender,
                         origin_name, location_name, image)

        db.session.add(char)

    db.session.commit()

    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)
