from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError
import os

# Initialize Flask app, SQLAlchemy database, and Marshmallow serializer
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///cultural_destinations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define Destination database model and schema for serialization/deserialization
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    contact = db.Column(db.String(100), nullable=True)
    website_url = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Destination {self.id}: {self.name}>'

class DestinationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Destination
        fields = ('id', 'name', 'description', 'image_url', 'location', 'contact', 'website_url', 'category')

# Define endpoints for creating and retrieving cultural destinations
@app.route('/destination', methods=['POST'])
def create_destination():
    destination_data = request.get_json()
    destination_schema = DestinationSchema()
    try:
        # Deserialize and validate destination data from request
        destination = destination_schema.load(destination_data, session=db.session)
        # Add destination to database
        db.session.add(destination)
        db.session.commit()
        # Serialize and return created destination
        result = destination_schema.dump(destination)
        return jsonify(result), 201
    except IntegrityError as e:
        # Handle unique constraint violation error
        db.session.rollback()
        return jsonify({'error': 'Destination name must be unique.'}), 400
    except Exception as e:
        # Handle any other error
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/destination', methods=['GET'])
def get_destinations():
    destination_schema = DestinationSchema(many=True)
    destinations = Destination.query.all()
    result = destination_schema.dump(destinations)
    return jsonify(result), 200

@app.route('/destination/<destination_id>', methods=['GET'])
def get_destination(destination_id):
    destination_schema = DestinationSchema()
    destination = Destination.query.get(destination_id)
    if destination:
        result = destination_schema.dump(destination)
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Destination not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
