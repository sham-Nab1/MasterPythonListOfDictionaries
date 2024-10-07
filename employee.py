# List of employee dictionaries
employees = [
    {"ID": 1, "Name": "John Doe", "Department": "Sales", "Age": 30, "Email": "john.doe@company.com"},
    {"ID": 2, "Name": "Jane Smith", "Department": "Human Resources", "Age": 25, "Email": "jane.smith@company.com"},
    {"ID": 3, "Name": "Mark Johnson", "Department": "IT", "Age": 40, "Email": "mark.johnson@company.com"},
    {"ID": 4, "Name": "Lisa Wong", "Department": "Marketing", "Age": 28, "Email": "lisa.wong@company.com"},
    {"ID": 5, "Name": "Paul McDonald", "Department": "Finance", "Age": 35, "Email": "paul.mcdonald@company.com"}
]

# Print employee data
for employee in employees:
    print(f"ID: {employee['ID']}, Name: {employee['Name']}, Department: {employee['Department']}, "
          f"Age: {employee['Age']}, Email: {employee['Email']},")
