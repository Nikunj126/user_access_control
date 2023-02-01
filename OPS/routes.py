from OPS.role_db_ops import *
from OPS.employee_db_ops import *


def initialize_routes(api):
    api.add_resource(GetRole, "/roles/get/<user_id>")
    api.add_resource(GetAllRoles, "/roles/get/all/<admin_id>")
    api.add_resource(AssignRole, "/roles/assign/<admin_id>")
    api.add_resource(UpdateRole, "/roles/update/<admin_id>&<user_id>")
    api.add_resource(DeleteRole, "/roles/delete/<admin_id>&<user_id>")
    api.add_resource(GetEmployee, "/employee/get/<emp_id>")
    api.add_resource(GetAllEmployees, "/employee/get/all/<user_id>")
    api.add_resource(AddEmployee, "/employee/add")
    api.add_resource(UpdateEmployee, "/employee/update/<user_id>&<emp_id>")
    api.add_resource(DeleteEmployee, "/employee/delete/<user_id>&<emp_id>")
