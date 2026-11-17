def read_notes():
    filename = "notes.txt"
    
    try:
        # Open and read all contents from the file
        with open(filename, "r") as file:
            contents = file.read()
            print("--- Contents of notes.txt ---")
            print(contents if contents.strip() else "The notes file is empty.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Run the function
read_notes()