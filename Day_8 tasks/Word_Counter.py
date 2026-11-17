def count_file_stats():
    filename = "article.txt"
    
    try:
        with open(filename, "r") as file:
            text = file.read()
            
        # Count characters, lines, and words
        char_count = len(text)
        lines = text.splitlines()
        line_count = len(lines)
        
        # Split by whitespace to get words
        words = text.split()
        word_count = len(words)
        
        print(f"--- File Statistics for {filename} ---")
        print(f"Characters: {char_count}")
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Run the function
count_file_stats()