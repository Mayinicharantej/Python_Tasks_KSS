# Loop to accept multiple log entries and append them safely
while True:
    action = input("Enter user action (or 'exit' to quit): ").strip()
    if action.lower() == "exit":
        break
    try:
        with open("activity.log", "a") as log_file:
            log_file.write(action + "\n")
        print("Logged.")
    except OSError as e:
        print("File error:", e)