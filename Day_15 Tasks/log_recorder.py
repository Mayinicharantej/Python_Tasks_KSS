# Generator yields one stripped line at a time without loading the whole file
def read_logs(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()


error_counts = {}

# Filter error entries and count occurrences in a dictionary
for line in read_logs("sample.log"):
    if "ERROR" in line:
        key = line.split("ERROR")[-1].strip() or "General Error"
        error_counts[key] = error_counts.get(key, 0) + 1

print(error_counts)