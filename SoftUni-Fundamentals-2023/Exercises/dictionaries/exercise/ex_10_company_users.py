company_data = {}
while True:
    command = input()
    if command == "End":
        break
    company_name, ID = command.split(" -> ")
    if company_name not in company_data.keys():
        company_data[company_name] = [ID]
    else:
        if ID not in company_data[company_name]:
            company_data[company_name].append(ID)
for company_name, ID in company_data.items():
    print(f"{company_name}")
    for employee in ID:
        print(f"-- {employee}")
