from models.department import Department
from models.employee import Employee
from os import system, name

def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
        
def return_to_main():
    advance = False
    while not advance:
        response = input("\nHit 'y' and <Enter> to return to the main menu...")
        if response.lower() == "y":
            advance = True
    clear_screen()
        

def action_msg(action, obj_ident=None, obj_desc=None, err_msg=None):
    # message components
    description = obj_desc.capitalize()
    identifier = f" '{obj_ident}' " if obj_ident else " "
    suffix = f": {err_msg}" if err_msg else ""

    return f"\n{description}{identifier}{action}{suffix}"


def user_prompt(obj_desc, obj_attrib):
    return f"Enter the {obj_desc}'s {obj_attrib} >> "


def exit_program():
    print("Goodbye!")
    exit()


# We'll implement the department functions in this lesson


def list_departments():
    clear_screen()
    print("List of all departments:\n")
    
    departments = Department.get_all()
   
    for department in departments:
        print(department)
    
    return_to_main()


def find_department_by_name():
    clear_screen()
    print("Find a department:\n")
    
    dept_name = input(user_prompt("department", "name"))
    
    if department := Department.find_by_name(dept_name):
        print(f"\n{department}")
    else:
        print(action_msg("not found", dept_name, "department"))
    
    return_to_main()


def find_department_by_id():
    clear_screen()
    print("Find a department:\n")
    
    dept_id = input(user_prompt("department", "ID"))
    
    if department := Department.find_by_id(dept_id):
        print(f"\n{department}")
    else:
        print(action_msg("not found", dept_id, "department"))
    
    return_to_main()


def create_department():
    clear_screen()
    print("Add new department to database:\n")
    
    dept_name = input(user_prompt("department", "name"))
    dept_location = input(user_prompt("department", "location"))
    
    try:
        department = Department.create(dept_name, dept_location)
        print(action_msg("creation succeeded", None, "department"))
        print(department)
    except Exception as exc:
        print(action_msg("creation failed", dept_name, "department", exc))
        
    return_to_main()

        
def update_department():
    clear_screen()
    print("Update department info:\n")
    
    dept_id = input(user_prompt("department", "ID"))
    
    if department := Department.find_by_id(dept_id):
        try:
            name = input(user_prompt("department", "name"))
            location = input(user_prompt("department", "location"))
            if name:
                department.name = name
            if location:
                department.location = location
            if name or location:
                department.update()
                print(action_msg("update succeeded", None, "department"))
                print(department)
        except Exception as exc:
           print(action_msg("update failed", None, "department", exc))
    else:
        print(action_msg("not found", dept_id, "department"))
        
    return_to_main()
           
     
def delete_department():
    clear_screen()
    print("Delete a department:\n")
    
    dept_id = input(user_prompt("department", "ID"))
    
    if department := Department.find_by_id(dept_id):
        department.delete()
        print(action_msg("deletion succeeded", dept_id, "departemt"))
    else:
        print(action_msg("not found", dept_id, "department"))

    return_to_main()


# You'll implement the employee functions in the lab

def list_employees():
    clear_screen()
    print("List of all employees:\n")
    
    employees = Employee.get_all()
   
    for employee in employees:
        print(employee)
    
    return_to_main()


def find_employee_by_name():
    clear_screen()
    print("Find an employee:\n")
    
    emp_name = input(user_prompt("employee", "name"))
    
    if employee := Employee.find_by_name(emp_name):
        print(f"\n{employee}")
    else:
        print(action_msg("not found", emp_name, "employee"))
    
    return_to_main()


def find_employee_by_id():
    clear_screen()
    print("Find an employee:\n")
    
    emp_id = input(user_prompt("employee", "ID"))
    
    if employee := Employee.find_by_id(emp_id):
        print(f"\n{employee}")
    else:
        print(action_msg("not found", emp_id, "employee"))
    
    return_to_main()


def create_employee():
    clear_screen()
    print("Add new employee to database:\n")
    
    emp_name = input(user_prompt("employee", "name"))
    emp_title = input(user_prompt("employee", "job title"))
    emp_dept_id = input(user_prompt("employee", "department"))
    
    try:
        employee = Employee.create(emp_name, emp_title, int(emp_dept_id))
        print(action_msg("creation succeeded", None, "employee"))
        print(employee)
    except Exception as exc:
        print(action_msg("creation failed", emp_name, "employee", exc))
        
    return_to_main()


def update_employee():
    clear_screen()
    print("Update employee info:\n")
    
    emp_id = input(user_prompt("employee", "ID"))
    
    if employee := Employee.find_by_id(emp_id):
        try:
            name = input(user_prompt("employee", "name"))
            title = input(user_prompt("employee", "job title"))
            dept_id = input(user_prompt("employee", "department ID"))
            if name:
                employee.name = name
            if dept_id:
                employee.department = int(dept_id)
            if title:
                employee.title = title
            if name or title or dept_id:
                employee.update()
                print(action_msg("update succeeded", None, "employee"))
                print(employee)
        except Exception as exc:
           print(action_msg("update failed", None, "employee", exc))
    else:
        print(action_msg("not found", emp_id, "employee"))
        
    return_to_main()


def delete_employee():
    clear_screen()
    print("Delete an employee:\n")
    
    emp_id = input(user_prompt("employee", "ID"))
    
    if employee := Employee.find_by_id(emp_id):
        employee.delete()
        print(action_msg("deletion succeeded", emp_id, "employee"))
    else:
        print(action_msg("not found", emp_id, "employee"))

    return_to_main()


def list_department_employees():
    clear_screen()
    print("Find a department:\n")
    
    dept_name = input(user_prompt("department", "name"))
    
    if department := Department.find_by_name(dept_name):
        print("")
        department.employees()
    else:
        print(action_msg("not found", dept_name, "department"))
    
    return_to_main()