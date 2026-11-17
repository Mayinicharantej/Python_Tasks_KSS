def manage_attendance():
    filename = "attendance.txt"
    
    # Take student name as input
    student_name = input("Enter student name to record attendance: ").strip()
    
    # Append the student's name to the file
    with open(filename, "a") as file:
        file.write(student_name + "\n")
        
    print(f"\nSuccessfully added '{student_name}' to {filename}.")
    print("--- Current Attendance Records ---")
    
    # Display the contents of the file
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content if content.strip() else "The file is currently empty.")
    except FileNotFoundError:
        print("No attendance records found yet.")

# Run the function
manage_attendance()
