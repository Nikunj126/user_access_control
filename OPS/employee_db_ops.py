from flask import Response, request
from flask_restful import Resource
import mongoengine
from OPS.has_access import *


class GetEmployee(Resource):
    def get(self, emp_id):
        try:
            roles = employee_db.objects.get(id=emp_id).to_json()
            return Response(roles, mimetype="application/json", status=200)
        except mongoengine.errors.ValidationError:
            res = emp_id + " does not exists."
            return Response(res, mimetype='application/json', status=404)


class GetAllEmployees(Resource):
    def get(self, user_id):
        try:
            role_type = ["ADMIN", "MASTERADMIN"]
            if has_access(user_id, role_type):
                roles = employee_db.objects().to_json()
                return Response(roles, mimetype="application/json", status=200)
            else:
                return "You don't have access to requested operation!!"
        except mongoengine.errors.ValidationError:
            res = "User ID " + user_id + " does not exists."
            return Response(res, mimetype='application/json', status=404)


class AddEmployee(Resource):
    def post(self):
        body = request.get_json()
        added_entry = employee_db(**body).save()
        emp_id = added_entry.id
        return 'Your employee_id is: ' + str(emp_id)


class UpdateEmployee(Resource):
    def put(self, user_id, emp_id):
        try:
            employee = employee_db.objects.get(id=emp_id)
            role_type = ["ADMIN", "MASTERADMIN"]
            body = request.get_json()
            if has_access(user_id, role_type):
                for field, value in body.items():
                    setattr(employee, field, value)
                    employee.save()
                return "Employee details has been successfully updated."
            else:
                return "You don't have access for requested operation."
        except mongoengine.errors.ValidationError:
            return "Either user ID or employee_id does not exists"
        except mongoengine.errors.NotUniqueError:
            return "Name is not unique, please try another."


class DeleteEmployee(Resource):
    def delete(self, user_id, emp_id):
        try:
            role_type = ["ADMIN", "MASTERADMIN"]
            if has_access(user_id, role_type):
                employee_db.objects.get(id=emp_id).delete()
                return 'Entry is successfully deleted', 200
            else:
                return "You don't have access for requested operation!!"
        except mongoengine.errors.ValidationError:
            res = "Either user ID or employee_id does not exists"
            return Response(res, mimetype='application/json', status=404)
