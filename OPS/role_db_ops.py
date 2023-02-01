from flask import Response, request
from flask_restful import Resource
import mongoengine
from OPS.has_access import *


class GetRole(Resource):
    def get(self, user_id):
        try:
            roles = role_db.objects.get(id=user_id).to_json()
            return Response(roles, mimetype="application/json", status=200)
        except mongoengine.errors.ValidationError:
            res = user_id + " does not exists."
            return Response(res, mimetype='application/json', status=404)


class GetAllRoles(Resource):
    def get(self, admin_id):
        try:
            role_type = ["MASTERADMIN"]
            if has_access(admin_id, role_type):
                roles = role_db.objects().to_json()
                return Response(roles, mimetype="application/json", status=200)
            else:
                return "You don't have access to requested operation!!"
        except mongoengine.errors.ValidationError:
            res = "Admin ID " + admin_id + " does not exists."
            return Response(res, mimetype='application/json', status=404)


class AssignRole(Resource):
    def post(self, admin_id):
        try:
            role_type = ["MASTERADMIN"]
            if has_access(admin_id, role_type):
                body = request.get_json()
                assigned_role = role_db(**body).save()
                user_id = assigned_role.id
                return {"User ID is: ": str(user_id)}, 200
            else:
                return "You don't have access to requested operation!!"
        except mongoengine.errors.NotUniqueError:
            res1 = "User_name is not unique, please try another."
            return Response(res1, mimetype='application/json', status=404)
        except mongoengine.errors.ValidationError:
            res2 = "Either the Admin ID " + admin_id + " does not exists or you've entered incorrect role_type." \
                    "role_type can only be a USER, ADMIN, MASTERADMIN"
            return Response(res2, mimetype='application/json', status=404)


class UpdateRole(Resource):
    def put(self, admin_id, user_id):
        try:
            role = role_db.objects.get(id=user_id)
            role_type = ["MASTERADMIN"]
            body = request.get_json()
            if has_access(admin_id, role_type):
                for field, value in body.items():
                    setattr(role, field, value)
                    role.save()
                return "Role has been successfully updated."
            else:
                return "You don't have access for requested operation."
        except mongoengine.errors.ValidationError:
            return "Either user ID or employee_id does not exists"
        except mongoengine.errors.NotUniqueError:
            return "User_name is not unique, please try another."



class DeleteRole(Resource):
    def delete(self, admin_id, user_id):
        role_type = ["MASTERADMIN"]
        if has_access(admin_id, role_type):
            role_db.objects.get(id=user_id).delete()
            return 'Entry is successfully deleted', 200
        else:
            return "You don't have access for requested operation!!"
