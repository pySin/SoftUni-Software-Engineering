# Company Users


def company_employees():

    employees_dict = {}
    command = input()

    while command != "End":

        employees = command.split(" -> ")
        if employees[0] not in employees_dict.keys():
            employees_dict[employees[0]] = {employees[1]: 0}
        else:
            employees_dict[employees[0]][employees[1]] = 0

        command = input()

    return employees_dict


for company, current_employees in company_employees().items():
    print(company)
    for employee in current_employees.keys():
        print(f"-- {employee}")
