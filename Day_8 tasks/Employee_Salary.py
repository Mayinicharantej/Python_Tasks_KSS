def employee_salary_system():
    filename = "employees.txt"
    
    # 1. Read and display employee data, and find the highest salary
    try:
        print("--- Employee Details ---")
        highest_salary = -1
        top_employee = ""
        has_data = False
        
        with open(filename, "r") as file:
            header = file.readline() # Read header
            print(header.strip() if header else "")
            
            for line in file:
                line = line.strip()
                if line:
                    has_data = True
                    print(line)
                    parts = line.split()
                    if len(parts) >= 2:
                        name = " ".join(parts[:-1])
                        try:
                            salary = float(parts[-1])
                            if salary > highest_salary:
                                highest_salary = salary
                                top_employee = name
                        except ValueError:
                            continue
                            
        if has_data and highest_salary != -1:
            print(f"\nEmployee with the highest salary: {top_employee} ({highest_salary})")
        else:
            print("\nNo employee records found.")
            
    except FileNotFoundError:
        print(f"Note: '{filename}' not found. A new file will be created upon appending.")
        
    # 2. Append a new employee record to the file
    print("\n--- Add New Employee ---")
    new_name = input("Enter Employee Name: ").strip()
    new_salary = input("Enter Salary: ").strip()
    
    with open(filename, "a") as file:
        file.write(f"{new_name} {new_salary}\n")
        
    print(f"Successfully added {new_name} to {filename}.")

# Run the function
employee_salary_system()