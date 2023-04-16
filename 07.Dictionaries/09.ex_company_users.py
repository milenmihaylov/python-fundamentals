companies_info = {}

information = input()
while not information == 'End':
    company_name, employee_id = information.split(' -> ')
    if company_name not in companies_info:
        companies_info[company_name] = []
    if employee_id not in companies_info[company_name]:
        companies_info[company_name].append(employee_id)

    information = input()

for company, employee_list in sorted(companies_info.items(), key=lambda x: x[0]):
    print(company)
    for employee in employee_list:
        print(f"-- {employee}")
