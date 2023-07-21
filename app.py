from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URL")
CORS(app, resources={
     "*": {"origins": ["https://react-to-api-python.vercel.app"]}})

db = SQLAlchemy(app)
ma = Marshmallow(app)


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


class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character


@app.route('/search', methods=['GET'])
def get_characters():
    page = int(request.args.get('page', 1))
    nameSearch = request.args.get('name', '')

    limit = 20

    characters = Character.query.filter(Character.name.ilike(f'%{nameSearch.lower()}%')) \
        .limit(limit) \
        .offset((page - 1) * limit) \
        .all()

    character_schema = CharacterSchema(many=True)
    result = character_schema.dump(characters)

    return jsonify({
        'characters': result,
        'total_pages': len(characters) // limit + 1,
        'current_page': page,
        'total_items': len(characters)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)
