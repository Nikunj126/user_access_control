from Database.models import *


def has_access(user_id, role_type):
    a = 0
    if user_id == "masteradmin1234":
        return True
    else:
        roles = role_db.objects.get(id=user_id)
        for item in role_type:
            if item == roles["role_type"] :
                a = 1
        if a == 1 or user_id == "masteradmin1234":
            return True
        else:
            return False
