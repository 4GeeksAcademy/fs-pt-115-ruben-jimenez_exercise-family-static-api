"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object// Crea el objeto de la familia Jackson.
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object // 
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints// Genera un sitemap con todos tus endpoints
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(jackson_family.get_all_members()), 200


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods// Así es como puedes utilizar la estructura de datos Family llamando a sus métodos.
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
  
        member = jackson_family.get_member(member_id)
        if not member:
            return jsonify({"message": "Member not found"}), 404
        return jsonify(member), 200
 

@app.route('/members', methods=['POST'])
def add_member():
  
        data = request.get_json()
        required = {"first_name", "age", "lucky_numbers"}
        if not data or not required.issubset(data.keys()):
            return jsonify({"message": "Missing or invalid fields"}), 400
        new_member = jackson_family.add_member(data)
        return jsonify(new_member), 200
   

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
  
    success = jackson_family.delete_member(member_id)
    if not success:
        return jsonify({"message": "Member not found"}), 404
    return jsonify({"done": True}), 200



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
