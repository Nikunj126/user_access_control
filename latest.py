class UpdateRole(Resource):
    def put(admin_id, user_id):
        role = role_db.objects(id=admin_id)
        role_type = ["MASTERMIND"]
        updates = request.get_json()
        if has_access(admin_id, role_type):
            for field, value in updates.items():
                setattr(role, field, value)
            role.save()
            return "Role has been updated successfully."
        else:
            return "You don't have access for requested operation!!"



class UpdateRole(Resource):
    def put(self, admin_id, user_id):
        try:
            role_type = ["MASTERADMIN"]
            body = request.get_json()
            if has_access(admin_id, role_type):
                role_db.objects.get(id=user_id).update(**body)
                return "Changes has been successfully saved.", 200
            else:
                return "You don't have access for requested operation."
        except mongoengine.errors.ValidationError:
            res = "Either user ID or employee_id does not exists"
            return Response(res, mimetype='application/json', status=404)
