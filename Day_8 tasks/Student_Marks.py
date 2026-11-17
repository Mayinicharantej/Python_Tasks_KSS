def analyze_student_marks():
    filename = "marks.txt"
    
    try:
        total_marks = 0
        count = 0
        
        print("--- Student Records ---")
        with open(filename, "r") as file:
            header = file.readline() # Read and skip header if present
            print(header.strip())
            
            for line in file:
                line = line.strip()
                if line:
                    print(line)
                    parts = line.split()
                    if len(parts) >= 2:
                        try:
                            marks = float(parts[-1])
                            total_marks += marks
                            count += 1
                        except ValueError:
                            continue
                            
        if count > 0:
            average_marks = total_marks / count
            print(f"\nClass Average Marks: {average_marks:.2f}")
        else:
            print("\nNo valid student marks found to calculate average.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Run the function
analyze_student_marks()