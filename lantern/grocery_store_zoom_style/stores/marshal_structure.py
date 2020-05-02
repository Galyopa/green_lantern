from flask_restful import fields

stores_structure = {
    "id": fields.Integer,
    "name": fields.String,
    "location": fields.String,
    "manager_id": fields.Integer,
}
